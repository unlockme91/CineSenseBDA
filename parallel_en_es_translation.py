from extract_spanish_subtitles import extract_spanish_subtitles
import time
import concurrent.futures


## This function is to run spanish transaltion task in multiple threads in parallel
##Param : {filenames} is the video titles/video folder and {text_list} is list of all extracted text
def es_subtitles_extraction_multiplethreads_pool(filenames,text_list):
    start=time.perf_counter()
    filename_text= list(zip(filenames, text_list))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_spanish_subtitles,filename_text)
    end=time.perf_counter()
    print(f'Parallel spanish translation(Threads pool): {end-start} second(s)')  