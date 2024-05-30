import load_video_URLs
import download_videos_serial
from  download_videos_parallel import download_video_urls_multiplethreads

def main():

    ## Loading the videos from the text file
    urls = load_video_URLs.load_urls('video_urls.txt')

    # Download videos into folder serieally
    # download_videos_serial.download_video_urls_serial(urls)

    
    ## Download videos into folder parallely
    download_video_urls_multiplethreads(urls)


if __name__ == "__main__":
    main()