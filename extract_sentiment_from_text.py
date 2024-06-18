from textblob import TextBlob

def extract_sentiment_from_text(filename_text):
    folder_title, text = filename_text[0], filename_text[1]
    file_path_sentiment = f'videos_processing_output/{folder_title}/extracted_sentiments.txt'
    blob = TextBlob(text)
    print(blob.sentiment)
    print(blob.sentiment.polarity)
    print(blob.sentiment.subjectivity)
    with open(file_path_sentiment, 'w') as file:
        file.write(str(blob.sentiment) +'\n')
        file.write('Polarity: ' + str(blob.sentiment.polarity) + '\n')
        file.write('Subjectivity: ' + str(blob.sentiment.subjectivity))
        
    print(f'Sentiment has been written to {file_path_sentiment}')