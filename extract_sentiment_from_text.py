from textblob import TextBlob

def extract_sentiment_from_text(video_title):
    file_path_text = f'videos_processing_output/{video_title}/extracted_text.txt'
    file_path_sentiment = f'videos_processing_output/{video_title}/extracted_sentiments.txt'
    with open(file_path_text, 'r') as fl:
        text = fl.read()
    blob = TextBlob(text)
    print(blob.sentiment)
    print(blob.sentiment.polarity)
    print(blob.sentiment.subjectivity)
    with open(file_path_sentiment, 'w') as file:
        file.write(str(blob.sentiment) +'\n')
        file.write('Polarity: ' + str(blob.sentiment.polarity) + '\n')
        file.write('Subjectivity: ' + str(blob.sentiment.subjectivity))
        
    print(f'Sentiment has been written to {file_path_sentiment}')