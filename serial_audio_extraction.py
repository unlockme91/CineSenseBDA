from extract_audio_from_video import extract_audio_from_video
import time

## This function is to run audio extraction task for every video sequentially
##Param : {filenames} is the list containing all the video titles/video file names
def audio_extraction_from_video_serial(filenames):
    start = time.perf_counter()
    for name in filenames: 
        extract_audio_from_video(name)
    end = time.perf_counter()
    print(f'Serial audio extraction(process poolmap): {end-start} second(s)') 
    