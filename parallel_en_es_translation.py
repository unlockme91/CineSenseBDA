from extract_spanish_subtitles import extract_spanish_subtitles
import time
import concurrent.futures


## This function is to run spanish transaltion task in multiple threads in parallel
##Param : {filenames_text} is the list of tuples, each tuple item containing the video title and its corresponding extracted text
def es_subtitles_extraction_multiplethreads_pool(filenames_text):
    start=time.perf_counter()
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(extract_spanish_subtitles,filenames_text)
    except Exception as e:
        print(f"Unexpected Error Found: {e}")     
    end=time.perf_counter()
    print(f'Parallel spanish translation(Threads pool): {end-start} second(s)')  