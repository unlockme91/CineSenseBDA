from pytube import YouTube
import threading

# Create a semaphore with a count of 5 to restrict simultaneous downloading to 5 videos avoid YouTube Blocks
video_download__semaphore = threading.Semaphore(5)

def download_videos_from_url(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    video_download__semaphore.acquire()
    try:
        print(f"Downloading video: {yt.title}")
        stream.download(output_path="video_output")
        print(f"Download completed: {yt.title}")
    finally:
        video_download__semaphore.release()