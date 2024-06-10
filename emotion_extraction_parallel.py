from extract_emotions_from_text import extract_emotions_from_text
import time
import multiprocessing

def emotion_extraction_multipleprocesses_pool(filenames,text_list):
    start=time.perf_counter()
    filename_text= list(zip(filenames, text_list))
    with multiprocessing.Pool() as pool:
        pool.map(extract_emotions_from_text,filename_text)
    end=time.perf_counter()
    print(f'Parallel emotion extraction(process poolmap): {end-start} second(s)')   