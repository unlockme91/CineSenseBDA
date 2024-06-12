from extract_emotions_from_text import extract_emotions_from_text
import time
import multiprocessing
import concurrent.futures

def emotion_extraction_multipleprocesses_pool(filenames,text_list):
    start=time.perf_counter()
    filename_text= list(zip(filenames, text_list))
    with multiprocessing.Pool() as pool:
        pool.map(extract_emotions_from_text,filename_text)
    end=time.perf_counter()
    print(f'Parallel emotion extraction(process poolmap): {end-start} second(s)') 

def emotion_extraction_multiplethreads(filenames,text_list):
    start=time.perf_counter()
    filename_text= list(zip(filenames, text_list))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_emotions_from_text,filename_text)
    end=time.perf_counter()
    print(f'Parallel emotion extraction(Threads pool): {end-start} second(s)')   