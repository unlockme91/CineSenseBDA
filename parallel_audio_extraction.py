from extract_audio_from_video import extract_audio_from_video
import multiprocessing
import concurrent.futures
import time

## This function is to run audio extraction task in multiple processes in parallel
##Param : {filename} is the video title/audio file path
def audio_extraction_multipleprocesses_pool(filenames):
    start=time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(extract_audio_from_video,filenames)
    end=time.perf_counter()
    print(f'Parallel audio extraction(process poolmap): {end-start} second(s)')       # Execution time is calculated


## This function is to run audio extraction task in multiple threads in parallel
##Param : {filename} is the video title/audio file path
def audio_extraction_multiplethreads(filenames):
    start=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_audio_from_video,filenames)
    end=time.perf_counter()
    print(f'Parallel audio extraction(Threads pool): {end-start} second(s)')    
