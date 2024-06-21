from nrclex import NRCLex

## This function is to extract emotions(as dictionary) from the text
##Param : {filename_text} is the tuple containing the video title and extracted text from the corresponding video
def extract_emotions_from_text(filename_text):
    folder_title, text = filename_text[0], filename_text[1]
    file_path_emotion = f'videos_processing_output/{folder_title}/extracted_emotions.txt'
    try:
        emotion = NRCLex(text) # Here the output is dictionary containing the diffrent emotions as key and value as their strength in video
        with open(file_path_emotion,'w') as fl:
            fl.write("Detected Emotions and Frequencies: \n" + str(emotion.affect_frequencies))
    except Exception as e:
        print(f"Unexpected Error Found: {e}")
