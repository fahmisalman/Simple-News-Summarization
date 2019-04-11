from Model.Preprocessing import Preprocessing


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


def fit(paragraph):

    pre = Preprocessing()

    sentence_list = sentence_split(paragraph)
    print(sentence_list)
    data = []
    for i in range(len(sentence_list)):
        data.append(pre.stemming(pre.stopword_removal(pre.tokenization(pre.casefolding(sentence_list[i])))))
    data = (list(filter(None, data)))

    wordfreq = word_freq(data)

    ranking = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        ranking.append(temp)

    sort_list = sorted(range(len(ranking)), key=ranking.__getitem__, reverse=True)
    n = 1
    sentence = ''
    for i in range(n):
        sentence += '{}. '.format(sentence_list[sort_list[i]])
    return sentence
