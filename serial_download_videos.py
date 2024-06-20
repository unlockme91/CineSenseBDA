import time
from download_video import download_videos_from_url

## This function is to download videos from every url sequentially
##Param : {urls} is the list containing all the video urls which will be iterated
def download_video_urls_serial(urls):
    start = time.perf_counter()
    [download_videos_from_url(url) for url in urls]
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

    

