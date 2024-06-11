import spacy,nltk
from nrclex import NRCLex
nlp = spacy.load('en_core_web_sm')
nltk.download('punkt')

def extract_emotions_from_text(filename_text):
    folder_title, text = filename_text[0], filename_text[1]
    file_path_emotion = f'videos_processing_output/{folder_title}/extracted_emotions.txt'
    doc = nlp(text)
    full_text = ' '.join([sent.text for sent in doc.sents])
    emotion = NRCLex(text)
    with open(file_path_emotion,'w') as fl:
        fl.write("Detected Emotions and Frequencies: \n" + str(emotion.affect_frequencies))
