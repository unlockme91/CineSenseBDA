from extract_text_from_audio import extract_text_from_audio
import time
import concurrent.futures
import multiprocessing


## This function is to run text extraction task in multiple processes in parallel
##Param : {filenames} is the list containing all the video titles/text file names
def text_extraction_multipleprocesses_pool(filenames):
    start=time.perf_counter()
    with multiprocessing.Pool() as executor:
        executor.map(extract_text_from_audio,filenames)
    end=time.perf_counter()
    print(f'Parallel text extraction(process poolmap): {end-start} second(s)')  



## This function is to run text extraction task in multiple threads in parallel
##Param : {filenames} is the list containing all the video titles/textfile names
def text_extraction_multiplethreads_pool(filenames):
    start=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        text_list = executor.map(extract_text_from_audio,filenames)
    end=time.perf_counter()
    print(f'Parallel text extraction(process poolmap): {end-start} second(s)')  
    return text_list
