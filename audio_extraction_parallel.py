from extract_audio_from_video import extract_audio_from_video
import multiprocessing
import concurrent.futures
import time

def audio_extraction_multipleprocesses_pool(filenames):
    start=time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(extract_audio_from_video,filenames)
    end=time.perf_counter()
    print(f'Parallel audio extraction(process poolmap): {end-start} second(s)')       

def audio_extraction_multiplethreads(filenames):
    start=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_audio_from_video,filenames)
    end=time.perf_counter()
    print(f'Parallel audio extraction(Threads pool): {end-start} second(s)')    
