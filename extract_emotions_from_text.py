import spacy,nltk
from nrclex import NRCLex
nlp = spacy.load('en_core_web_sm')
nltk.download('punkt')

def extract_emotions_from_text(filename_text):
    file_path_emotion = f'videos_processing_output/{filename_text[0]}/extracted_emotions.txt'
    doc = nlp(filename_text[1])
    full_text = ' '.join([sent.text for sent in doc.sents])
    emotion = NRCLex(filename_text[1])
    print("Detected Emotions and Frequencies:")
    print(emotion.affect_frequencies)