from nltk.corpus import stopwords
import re


def casefolding(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
    return sentence


def tokenization(sentence):
    return sentence.split()


def stopword_removal(token):
    stopWords = set(stopwords.words('english'))
    wordsFiltered = []
    for w in token:
        if w not in stopWords:
            wordsFiltered.append(w)
    return wordsFiltered