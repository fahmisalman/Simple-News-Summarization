from Preprocessing import *


__author__ = "Fahmi Salman Nurfikri"


def sentence_split(paragraph):
    j = 0
    data = []
    for i in range(len(paragraph)):
        if paragraph[i] == '.':
            data += (list(filter(None, paragraph[j:i].rsplit('\n'))))
            j = i + 1
    return data


def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res


def summarizer(paragraph):

    sentence_list = sentence_split(paragraph)
    data = []
    for i in range(len(sentence_list)):
        data.append(stemming(stopword_removal(tokenization(casefolding(sentence_list[i])))))
    data = (list(filter(None, data)))

    wordfreq = word_freq(data)

    ranking = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        ranking.append(temp)

    sortList = sorted(range(len(ranking)), key=ranking.__getitem__, reverse=True)
    n = 3
    sentence = ''
    for i in range(n):
        sentence += '{}. '.format(sentence_list[sortList[i]])
    return sentence
