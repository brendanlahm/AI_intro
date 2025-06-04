################################################################## Information Retrieval
import nltk
import pickle
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

with open('./wine_lines.data', 'rb') as filehandle:
    wine_reviews = pickle.load(filehandle)

########################################## Task 1: Tokenizing words from a messy data file
reviews_tokenized = []
from nltk.tokenize import word_tokenize #TODO: find the function for word level tokenization

for review in wine_reviews:
    tokenized = word_tokenize(review, language = 'english') #TODO tokenized the review here
    reviews_tokenized.append(tokenized)

# TODO check the content of the first 10 tokenized reviews, maybe choose another review
print("\nFirst 10 tokenized reviews")
print(reviews_tokenized[0:10])

########################################## Task 2: Stemmer & Lemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import EnglishStemmer, PorterStemmer, SnowballStemmer

reviews_stemmed = []
reviews_lemmatized = []
stemmer = EnglishStemmer()
lemmatizer = WordNetLemmatizer()

import re

for tokenized_review in reviews_tokenized:
    #cleaned_tokens = [token for token in tokenized_review if not re.match(r'^</?.*>?$', token)]
    cleaned_tokens = [token for token in tokenized_review if not (token.startswith('<') and token.endswith('>'))]
    stemmed = [stemmer.stem(token) for token in cleaned_tokens]
    lemmatized = [lemmatizer.lemmatize(token) for token in cleaned_tokens]
    reviews_stemmed.append(stemmed)
    reviews_lemmatized.append(lemmatized)
    
print(reviews_stemmed[0:10], sep="\n")
print(reviews_lemmatized[0:10], sep="\n")

########################################## Stack 3: Removing stop words
from nltk.corpus import stopwords
from string import punctuation
print(list(punctuation))
reviews_cleaned = []
stopwords = stopwords.words()

# TODO: add relevant punctuation to the stopwords list
# TODO filter out stopwords and punctuation for each review
for review in reviews_stemmed:
    reviews_cleaned.append([w for w in review if w not in stopwords])
    pass #TODO remove after you added code

print(reviews_cleaned[:10])







