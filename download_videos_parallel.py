from download_video import download_videos_from_url
import concurrent.futures
import time

def download_video_urls_multiplethreads(urls):
     start=time.perf_counter()
     with concurrent.futures.ThreadPoolExecutor() as executor:
          file_titles = executor.map(download_videos_from_url, urls) 
     end = time.perf_counter()
     print(f'Parallel (thread pool map): {end - start} second(s)')
     return file_titles
     