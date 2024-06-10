from textblob import TextBlob
from googletrans import Translator


def extract_spanish_subtitles(video_title):
    file_path_text = f'videos_processing_output/{video_title}/extracted_text.txt'
    file_path_subtitles = f'videos_processing_output/{video_title}/extracted_spanish_subtitles.txt'
    translator = Translator()
    with open(file_path_text, 'r') as fl:
        text = fl.read()
    blob_translated = translator.translate(text,src='en', dest='es')
    with open(file_path_subtitles, 'w') as file:
        text = file.write(blob_translated.text)