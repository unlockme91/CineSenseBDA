from extract_text_from_audio import extract_text_from_audio
import time
import concurrent.futures
import multiprocessing

def text_extraction_multipleprocesses_pool(filenames):
    start=time.perf_counter()
    with multiprocessing.Pool() as executor:
        text_list = executor.map(extract_text_from_audio,filenames)
    end=time.perf_counter()
    print(f'Parallel text extraction(process poolmap): {end-start} second(s)')  
    return text_list
