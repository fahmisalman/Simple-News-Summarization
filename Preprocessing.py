from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re


factory = StemmerFactory()
stemmer = factory.create_stemmer()


def casefolding(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
    return sentence


def tokenization(sentence):
    return sentence.split()


def stopword_removal(token):
    stopword = [line.rstrip('\n\r') for line in open('stopwords.txt')]
    temp = []
    for i in range(len(token)):
        if token[i] not in stopword:
            temp.append(token[i])
    return temp


def stemming(self, token):
    return self.stemmer.stem(token)
