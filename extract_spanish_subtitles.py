from googletrans import Translator

## This function is to transalate extracted english text into spanish
##Param : {filename_text} is the tuple containing the video title and extracted text from the corresponding video
def extract_spanish_subtitles(filename_text):
    folder_title, text = filename_text[0], filename_text[1]
    file_path_subtitles = f'videos_processing_output/{folder_title}/extracted_spanish_subtitles.txt'
    try:
        translator = Translator()
        translated_obj = translator.translate(text,src='en', dest='es')
        with open(file_path_subtitles, 'w') as file:
            file.write(translated_obj.text)
        print(f'Spanish Subtitles has been written to {file_path_subtitles}')
    except Exception as e:
        print(f"Unexpected Error Found: {e}")