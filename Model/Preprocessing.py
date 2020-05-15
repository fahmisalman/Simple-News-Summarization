# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import os


class Preprocessing(object):

    def __init__(self):
        # self.factory = StemmerFactory()
        # self.stemmer = self.factory.create_stemmer()
        self.stopwords = [line.rstrip('\n\r') for line in open(os.path.join(os.getcwd(), 'Model/stopwords.txt'))]

    def casefolding(self, sentence):
        sentence = sentence.lower()
        sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
        return sentence

    def tokenization(self, sentence):
        return sentence.split()

    def stopword_removal(self, token):
        temp = []
        for i in range(len(token)):
            if token[i] not in self.stopwords:
                temp.append(token[i])
        return temp

    # def stemming(self, tokens):
    #     for i in range(len(tokens)):
    #         tokens[i] = self.stemmer.stem(tokens[i])
    #     return tokens
