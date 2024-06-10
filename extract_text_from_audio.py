import speech_recognition as sr


def extract_text_from_audio(video_title):
    recognizer = sr.Recognizer()
    with sr.AudioFile(f"videos_processing_output/{video_title}/extracted_audio.wav") as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    file_path = f'videos_processing_output/{video_title}/extracted_text.txt'
    with open(file_path, 'w') as file:
        file.write(text)
    print(f'Text has been written to {file_path}')
    return text