from extract_audio_from_video import extract_audio_from_video
import time


def audio_extraction_from_video_serial(filenames):
    start = time.perf_counter()
    for name in filenames:
        extract_audio_from_video(name)
    end = time.perf_counter()
    print(f'Serial audio extraction(process poolmap): {end-start} second(s)') 
    