import os
import parallel_audio_extraction
import load_video_URLs
import serial_download_videos
from  parallel_download_videos import download_video_urls_multiplethreads
from serial_audio_extraction import audio_extraction_from_video_serial
from parallel_text_extraction import text_extraction_multipleprocesses_pool,text_extraction_multiplethreads_pool
from parallel_sentiment_extraction import sentiment_extraction_multiplethreads_pool
from parallel_en_es_translation import es_subtitles_extraction_multiplethreads_pool
from parallel_emotion_extraction import  emotion_extraction_multiplethreads
from extract_spanish_subtitles import extract_spanish_subtitles



def main():

    # Loading the videos from the text file
    urls = load_video_URLs.load_urls('video_urls.txt')

    # Download videos into folder serieally
    serial_download_videos.download_video_urls_serial(urls)

    
    # Download videos into folder parallely using multithreads
    download_video_urls_multiplethreads(urls)

    filenames=  []
    for file in os.listdir('video_output'):
        filenames.append(os.path.splitext(file)[0])

    # Extracts the audio file `wav` from a video clip `mp4` sequentially
    audio_extraction_from_video_serial(filenames)

    # Extracts the audio file `wav` from a video clip `mp4` by using multiple processes
    parallel_audio_extraction.audio_extraction_multipleprocesses_pool(filenames)

    # Extracts the audio file `wav` from a video clip `mp4` by using multiple threads
    parallel_audio_extraction.audio_extraction_multiplethreads(filenames)

    # Extracts the text file `txt` from a audio clip `wav` by using multiple processes
    text_list = text_extraction_multipleprocesses_pool(filenames)

    # Extracts the text file `txt` from a audio clip `wav` by using multiple threads
    text_list = text_extraction_multiplethreads_pool(filenames)


    # Extracts the sentiments from the extracted text by using multiple threads
    sentiment_extraction_multiplethreads_pool(filenames,text_list)



    # Extracts the spanish subtitles from the extracted english text using multiple threads
    es_subtitles_extraction_multiplethreads_pool(filenames,text_list)


    # Extracts the emotions from the extracted english text using multiple threads
    emotion_extraction_multiplethreads(filenames,text_list)




if __name__ == "__main__":
    main()