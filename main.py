import audio_extraction_parallel
import load_video_URLs
import download_videos_serial
from  download_videos_parallel import download_video_urls_multiplethreads
from audio_extraction_serial import audio_extraction_from_video_serial
from text_extraction_parallel import text_extraction_multipleprocesses_pool
from sentiment_extraction_parallel import sentiment_extraction_multipleprocesses_pool
import os

def main():

    # Loading the videos from the text file
    urls = load_video_URLs.load_urls('video_urls.txt')

    # Download videos into folder serieally
    download_videos_serial.download_video_urls_serial(urls)

    
    # Download videos into folder parallely
    download_video_urls_multiplethreads(urls)

    filenames=  []
    for file in os.listdir('video_output'):
        filenames.append(os.path.splitext(file)[0])

    # Extracts the audio file `wav` from a video clip `mp4` sequentially
    audio_extraction_from_video_serial(filenames)

    # Extracts the audio file `wav` from a video clip `mp4` by using multiple processes
    audio_extraction_parallel.audio_extraction_multipleprocesses_pool(filenames)

    # Extracts the audio file `wav` from a video clip `mp4` by using multiple processes
    audio_extraction_parallel.audio_extraction_multiplethreads(filenames)

    # Extracts the text file `wav` from a audio clip `wav` by using multiple processes
    text_extraction_multipleprocesses_pool(filenames)

    # Extracts the text file `wav` from a audio clip `wav` by using multiple processes
    sentiment_extraction_multipleprocesses_pool(filenames)


if __name__ == "__main__":
    main()