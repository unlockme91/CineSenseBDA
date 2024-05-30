import load_video_URLs
import download_videos

def main():

    # Loading the videos from the text file
    urls = load_video_URLs.load_urls('video_urls.txt')

    #Download videos into file
    download_videos.download_video_urls(urls)


if __name__ == "__main__":
    main()