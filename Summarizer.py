from nltk.corpus import stopwords
import re


def sentence_split(paragraph):
    j = 0
    data = []
    for i in range(len(paragraph)):
        if paragraph[i] == '.':
            data += (list(filter(None, paragraph[j:i].rsplit('\n'))))
            j = i + 1
    return data


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

if __name__ == '__main__':

    paragraph = '''Like a bowling ball on a skating rink, the black geodesic sphere of the East Greenland Ice-Core Project’s communal living space stands out against the endless white nothingness of the Greenland ice sheet.

    But the real action at East GRIP is under the surface. Researchers are drilling through more than 2.5 kilometers of ice, down to the bedrock below. The ice is sliding fast — for a glacier — toward the sea. Scientists here want to know why. The answer may hold clues to the future of the world’s coastal cities.

    Greenland is melting. As it melts, it adds roughly 1 millimeter of water per year to global sea levels. And the pace of melting is quickening.

    If all the ice covering the world’s largest island were to thaw, sea levels would rise roughly 6 meters. Scientists don’t know how fast, or how likely, that is to happen. East GRIP is looking for evidence to inform both those questions.

    The answers are a matter of growing urgency. The seas are rising faster. And the same processes at work on Greenland’s glaciers at the top of the world could send vast sections of Antarctica’s ice sheet into the sea as well, raising ocean levels even further.

    
    The Arctic is warming twice as fast as the rest of the planet. Scientists studying the rapid changes gather in the small Greenland town of Kangerlussuaq, a former U.S. military base built during World War II. Through the Cold War, this outpost supplied remote radar sites watching for a nuclear attack coming over the pole.

    These days, military transport planes fly scientists and their equipment across 1,000 kilometers of Arctic ice to East GRIP. They make research possible here and at other far-flung scientific outposts on the vast Greenland ice sheet.

    Departing from Kangerlussuaq, VOA visited East GRIP and other remote corners of Greenland with the 109th Airlift Wing of the U.S. Air National Guard for a firsthand look at science in action at the leading edge of climate change.'''

    sentence_list = sentence_split(paragraph)
    data = []
    for i in range(len(sentence_list)):
        data.append(stopword_removal(tokenization(casefolding(sentence_list[i]))))
    data = (list(filter(None, sentence_list)))

    wordfreq = word_freq(data)

    ranking = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        ranking.append(temp)

    sortList = sorted(range(len(ranking)),key=ranking.__getitem__, reverse=True)
    n = 3
    for i in range(n):
        print('{}.'.format(sentence_list[sortList[i]]), end=' ')
    print()

'''https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/'''