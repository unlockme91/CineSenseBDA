import speech_recognition as sr

## This function is to extract text from audio
##Param : {video_title} is the title of the video and folder name here
## This function will return extracted text of all videos

def extract_text_from_audio(video_title):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(f"videos_processing_output/{video_title}/extracted_audio.wav") as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        file_path = f'videos_processing_output/{video_title}/extracted_text.txt'
        with open(file_path, 'w') as file:
            file.write(text)
        print(f'Text has been written to {file_path}')
        return text
    except Exception as e:
        print(f"Unexpected Error Found: {e}")