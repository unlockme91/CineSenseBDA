import moviepy.editor as mp
import os
from pathlib import Path

## This function is to extract audio from video
##Param : {filename} is the video title
def extract_audio_from_video(filename):
    folder_name = filename
    file_mp4 = filename + ".mp4"
    try:
        filepath_video = os.path.join('video_output',file_mp4 )
        folder_audio = Path(f"videos_processing_output/{folder_name}")
        folder_audio.mkdir(parents=True, exist_ok=True)
        filepath_audio = f"{folder_audio}/extracted_audio.wav"
        video = mp.VideoFileClip(filepath_video)
        video.audio.write_audiofile(filepath_audio)

    except FileNotFoundError as e:
        print(f"{filename}.mp4 File not found: {e}")
    except Exception as e:
        print(f"Unexpected Error Found: {e}")
