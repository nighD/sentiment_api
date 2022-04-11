SENTIMENT ANALYSIS API
Basic Algorithm:

NaiveBayesClassifier was used as the opinion classifier.

The dataset included a list of sentences.

The sentences was converted to form bag of words.

The training model was created based on Twitter dataset.

After training, the model will be used to export results from the api's input.

Run:
Run command to serve server: 
uvicorn sentiment-api:app --reload


Testing:

http://127.0.0.1:8000/sentiment/

Body: 

{
  "text": "this is bad day =) =) =)"
}