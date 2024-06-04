import moviepy.editor as mp
import os
from pathlib import Path


def extract_audio_from_video(filename):
    folder_name = filename
    file_mp4 = filename + ".mp4"
    try:
        filepath_video = os.path.join('video_output',file_mp4 )
        folder_audio = Path("videos_processing_output/abc").mkdir(parents=True, exist_ok=True)
        filepath_audio = f"{folder_audio}/extracted_audio.wav"
        video = mp.VideoFileClip(filepath_video)
        video.audio.write_audiofile(filepath_audio)

    except Exception as e:
        print(e)
