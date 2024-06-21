from textblob import TextBlob


## This function is to extract sentiments from text
##Param : {filename_text} is the tuple containing the title of video and its corresponding extracted text

def extract_sentiment_from_text(filename_text):
    folder_title, text = filename_text[0], filename_text[1] # First element contains title of video and second contains text
    file_path_sentiment = f'videos_processing_output/{folder_title}/extracted_sentiments.txt'

    try:
        blob = TextBlob(text)
        print(blob.sentiment)
        print(blob.sentiment.polarity)
        print(blob.sentiment.subjectivity)
        with open(file_path_sentiment, 'w') as file:
            file.write(str(blob.sentiment) +'\n') #All attributes needs to be converted to string before writing them on file
            file.write('Polarity: ' + str(blob.sentiment.polarity) + '\n')
            file.write('Subjectivity: ' + str(blob.sentiment.subjectivity))
        
        print(f'Sentiment has been written to {file_path_sentiment}')
    except Exception as e:
        print(f"Unexpected Error Found: {e}")    