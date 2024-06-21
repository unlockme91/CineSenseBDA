from extract_sentiment_from_text import extract_sentiment_from_text
import time
import concurrent.futures


## This function is to run spanish transaltion task sentiment extraction task in multiple threads in parallel
##Param : {filename_text} is the tuple containing the video title and extracted text from the corresponding video
def sentiment_extraction_multiplethreads_pool(filename_text):
    start=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract_sentiment_from_text,filename_text)
    end=time.perf_counter()
    print(f'Parallel sentiments extraction(Threads Pool): {end-start} second(s)') 