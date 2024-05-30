
from download_video import download_videos_from_url
def download_video_urls_serial(urls):
    [download_videos_from_url(url) for url in urls]

    

