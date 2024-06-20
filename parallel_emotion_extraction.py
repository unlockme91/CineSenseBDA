from extract_emotions_from_text import extract_emotions_from_text
import time
import concurrent.futures


## This function is to run audio extraction task in multiple threads in parallel
##Param : {filenames} is the video titles and {text_list} is list of all extracted text
def emotion_extraction_multiplethreads(filenames,text_list):
    start=time.perf_counter()
    filename_text= list(zip(filenames, text_list)) #title of video and its corresponding text has been zipped into list of tuples
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_emotions_from_text,filename_text)
    end=time.perf_counter()
    print(f'Parallel emotion extraction(Threads pool): {end-start} second(s)')   