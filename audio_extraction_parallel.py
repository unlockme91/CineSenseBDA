from extract_audio_from_video import extract_audio_from_video
import multiprocessing
import time

def audio_extraction_multipleprocesses_pool(files):
    start=time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(extract_audio_from_video,files)
    end=time.perf_counter()
    print(f'Parallel (process poolmap): {end-start} second(s)')       
