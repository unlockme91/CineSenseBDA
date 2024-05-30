from pytube import YouTube

def download_videos_from_url(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading video: {yt.title}")
    stream.download(output_path="video_output")
    print(f"Download completed: {yt.title}")