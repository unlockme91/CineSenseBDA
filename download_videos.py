from pytube import YouTube

def download_video_urls(urls):

    yts = [YouTube(url) for url in urls]
    for yt in yts:
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading video: {yt.title}")
        stream.download(output_path="video_output")
        print(f"Download completed: {yt.title}")