import nltk
import nltk.classify.util
from nltk.corpus import twitter_samples
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import pickle
import itertools
from nltk.tokenize import word_tokenize 

nltk.download('punkt')

def create_word_features(words):
	score = BigramAssocMeasures.chi_sq

	#bigram count
	n = 600

	bigram_finder = BigramCollocationFinder.from_words(words)
	bigrams = bigram_finder.nbest(score, n)
	return dict([(word, True) for word in itertools.chain(words, bigrams)])
	
	return dict([(word, True) for word in words])


def create_model():
  positive_temp_tweets = twitter_samples.strings('positive_tweets.json')
  negative_temp_tweets = twitter_samples.strings('negative_tweets.json')

  positive_tweets = []
  negative_tweets = []

  for word in positive_temp_tweets:

    str = ""
    j = 0
    while(j < len(word)):
      if(word[j] == '@'):
        while(j < len(word) and word[j] != ' ' and word[j] != '\n'):
          j += 1

      if(j < len(word)):
        str += word[j]

      j += 1

    positive_tweets.append((create_word_features(word_tokenize(str)), "positive"))


  for word in negative_temp_tweets:
    str = ""
    j = 0
    while(j < len(word)):
      if(word[j] == '@'):
        while(j < len(word) and word[j] != ' ' and word[j] != '\n'):
          j += 1
      if(j < len(word)):
        str += word[j]

      j += 1

    negative_tweets.append((create_word_features(word_tokenize(str)), "negative"))


  train_set = negative_tweets[:4000] + positive_tweets[:4000]
  test_set = negative_tweets[4000:] + positive_tweets[4000:]


  #Run next 4 instructions if you're running the script for first time 
  # classifier = NaiveBayesClassifier.train(train_set)
  # classify_buffer = open('training_model.pickle', 'wb')
  # pickle.dump(classifier, classify_buffer)
  # classify_buffer.close()
  #Comment above 4 instructions if you've run the script once

  #Run next 3 instructions if you're running the script second time onwards
  classify_buffer = open('training_model.pickle', 'rb')
  classifier = pickle.load(classify_buffer)
  classify_buffer.close()
  #Comment aboce 3 instructions while running the script for first time
  return classifier

  # input_sample = 'today is a shit day =))))'
  
  # print(classifier.classify(input_sample_features))

  # print("Accuracy is :", nltk.classify.util.accuracy(classifier, test_set) * 100)