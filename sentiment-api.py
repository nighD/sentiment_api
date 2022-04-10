from fastapi import FastAPI
from pydantic import BaseModel
from training_model import create_word_features, create_model
from nltk.tokenize import word_tokenize

class Item(BaseModel):
    text: str

app = FastAPI()
trainingModel = create_model()

@app.get('/sentiment/')
async def query_sentiment_analysis(item: Item):
    return analyze_sentiment(item)


def analyze_sentiment(item):
    """Get and process result"""
    
    input_sample_features = create_word_features(word_tokenize(item.text))
    result = trainingModel.classify(input_sample_features)

    sent = ''
    if (result == 'positive'):
        sent = 'happy'
    else:
        sent = 'sad'

    # # Format and return results
    return {'sentiment': sent, 'message': item.text}