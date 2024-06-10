from extract_sentiment_from_text import extract_sentiment_from_text
import time
import multiprocessing

def sentiment_extraction_multipleprocesses_pool(filenames):
    start=time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(extract_sentiment_from_text,filenames)
    end=time.perf_counter()
    print(f'Parallel sentiments extraction(process poolmap): {end-start} second(s)') 