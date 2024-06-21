from extract_emotions_from_text import extract_emotions_from_text
import time
import concurrent.futures


## This function is to run emotion extraction task in multiple threads in parallel
##Param : {filenames_text} is the list of tuples, each tuple item containing the video title and its corresponding extracted text
def emotion_extraction_multiplethreads(filenames_text):
    start=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_emotions_from_text,filenames_text)
    end=time.perf_counter()
    print(f'Parallel emotion extraction(Threads pool): {end-start} second(s)')   