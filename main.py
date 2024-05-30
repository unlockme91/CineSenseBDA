import load_video_URLs
import download_videos_serial

def main():

    # Loading the videos from the text file
    urls = load_video_URLs.load_urls('video_urls.txt')

    #Download videos into file
    download_videos_serial.download_video_urls_serial(urls)


if __name__ == "__main__":
    main()