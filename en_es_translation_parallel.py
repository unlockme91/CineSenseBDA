from extract_spanish_subtitles import extract_spanish_subtitles
import time
import multiprocessing

def es_subtitles_extraction_multipleprocesses_pool(filenames,text_list):
    start=time.perf_counter()
    filename_text= list(zip(filenames, text_list))
    with multiprocessing.Pool() as pool:
        pool.map(extract_spanish_subtitles,filename_text)
    end=time.perf_counter()
    print(f'Parallel subtitles extraction(process poolmap): {end-start} second(s)') 