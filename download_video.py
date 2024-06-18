from pytube import YouTube, exceptions
import threading
from datetime import datetime

# Create a semaphore with a count of 5 to restrict simultaneous downloading to 5 videos avoid YouTube Blocks
video_download__semaphore = threading.Semaphore(5)
mutex = threading.Lock()


## This function is to download the best available stream
## {url} is the video urls
def download_videos_from_url(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        try:
            video_download__semaphore.acquire()
            print(f"Downloading video: {yt.title}")
            stream.download(output_path="video_output")
            timestamp = datetime.now().strftime("%H:%M, %d %b %Y")
            print(f"Download completed: {yt.title}")
            log_data = f'''"Timestamp": {timestamp}, "URL": {url}, "Download":True\n'''
            mutex.acquire()
            with open('download_log.txt', 'a') as fl:
                fl.write(log_data)
            return yt.title
        ## both the mutex and semaphore will be released in finally in case if there is an exception
        finally:
            mutex.release()
            video_download__semaphore.release() 
    except exceptions.VideoUnavailable as e:
        with open('download_log.txt', 'a') as fl:
            fl.write(f'''"Timestamp": {datetime.now().strftime("%H:%M, %d %b %Y")}, "URL": {url}, "Download":False, "Error": {e}\n''') 
        