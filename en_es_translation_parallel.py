from extract_spanish_subtitles import extract_spanish_subtitles
import time
import multiprocessing

def es_subtitles_extraction_multipleprocesses_pool(filenames):
    start=time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(extract_spanish_subtitles,filenames)
    end=time.perf_counter()
    print(f'Parallel subtitles extraction(process poolmap): {end-start} second(s)') 