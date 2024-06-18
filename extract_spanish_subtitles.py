from googletrans import Translator


def extract_spanish_subtitles(filename_text):
    folder_title, text = filename_text[0], filename_text[1]
    file_path_subtitles = f'videos_processing_output/{folder_title}/extracted_spanish_subtitles.txt'
    translator = Translator()
    translated_obj = translator.translate(text,src='en', dest='es')
    with open(file_path_subtitles, 'w') as file:
        text = file.write(translated_obj.text)