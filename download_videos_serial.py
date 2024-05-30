import time
from download_video import download_videos_from_url
def download_video_urls_serial(urls):
    start = time.perf_counter()
    [download_videos_from_url(url) for url in urls]
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

    

