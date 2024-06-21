from extract_spanish_subtitles import extract_spanish_subtitles
import time
import concurrent.futures


## This function is to run spanish transaltion task in multiple threads in parallel
##Param : {filenames} is the video titles/video folder and {text_list} is list of all extracted text
def es_subtitles_extraction_multiplethreads_pool(filename_text):
    start=time.perf_counter()
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(extract_spanish_subtitles,filename_text)
    except Exception as e:
        print(f"Unexpected Error Found: {e}")     
    end=time.perf_counter()
    print(f'Parallel spanish translation(Threads pool): {end-start} second(s)')  