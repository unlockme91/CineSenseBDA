from textblob import TextBlob

def extract_sentiments_from_text(video_title):
    file_path = f'videos_processing_output/{video_title}/extracted_sentiments.txt'
    blob = TextBlob(text)
    print(blob.sentiment)
    print(blob.sentiment.polarity)
    print(blob.sentiment.subjectivity)
    with open(file_path, 'w') as file:
        file.write(blob.sentiment + '\n')
        file.write('Polarity: ' + blob.sentiment.polarity + '\n')
        file.write('Subjectivity: ' + blob.sentiment.subjectivity)
        
    print(f'Sentiment has been written to {file_path}')