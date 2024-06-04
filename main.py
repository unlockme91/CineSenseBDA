import audio_extraction_parallel
import load_video_URLs
import download_videos_serial
from  download_videos_parallel import download_video_urls_multiplethreads
import os

def main():

    ## Loading the videos from the text file
    urls = load_video_URLs.load_urls('video_urls.txt')

    # # Download videos into folder serieally
    download_videos_serial.download_video_urls_serial(urls)

    
    ## Download videos into folder parallely
    download_video_urls_multiplethreads(urls)

    filenames=  []
    for file in os.listdir('video_output'):
        filenames.append(os.path.splitext(file)[0])


    # ## Extracts the audio file `wav` from a video clip `mp4` by using multiple processes
    audio_extraction_parallel.audio_extraction_multipleprocesses_pool(filenames)


if __name__ == "__main__":
    main()