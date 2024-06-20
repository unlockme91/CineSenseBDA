from download_video import download_videos_from_url
import concurrent.futures
import time


## This function is to download videos in multiple threads in parallel
##Param : {urls} is the list containing videos urls
# returns the video titles which can be used further for folder creation
def download_video_urls_multiplethreads(urls):
     start=time.perf_counter()
     with concurrent.futures.ThreadPoolExecutor() as executor:
          file_titles = executor.map(download_videos_from_url, urls) #file_titles is the list of video titles received
     end = time.perf_counter()
     print(f'Parallel (thread pool map): {end - start} second(s)')
     return file_titles
     