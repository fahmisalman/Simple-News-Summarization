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
        data.append(stopword_removal(tokenization(casefolding(sentence_list[i]))))
    data = (list(filter(None, sentence_list)))

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


def scrapper():
    print()


if __name__ == '__main__':

    paragraph = '''Penonton Kejuaraan Dunia Motocross MXGP Disarankan Beli Tiket Online
Jakarta - Gelaran Kejuaraan Dunia Motorcross MXGP di Pangkalpinang tinggal 11 hari lagi. Agar tak ketinggalan kesempatan untuk menyaksikan langsung, penonton disarankan untuk memesan tiket secara online. 

Kejuaraan Dunia Motorcross MXGP yang merupakan seri kedua itu akan dihelat di area Sport Center GOR Sahabudin, Pangkalpinang, Bangka Belitung. Agenda tersebut digeber selama dua hari, Sabtu (4/3/2017) dan Minggu (5/3/2017). Selain MXGP, dalam ajang itu juga digeber kategori MX2, dan MX Women. 

Untuk bisa menyaksikan secara langsung aksi para crosser dunia itu, panitia penyelenggara menawarkan tiket dengan berbagai pilihan. Yakni, kelas VIP seharga Rp 3,5 juta. Pemilik tiket bisa nonton aksi para crosses dalam dua hari sekaligus mendapatkan konsumsi saat perlombaan. 

Kemudian tiket tribun yang diberi banderol harga Rp 700 ribu. Bedanya, penonton kategori ini tak mendapatkan konsumsi. 

"Kategori ketiga adalah kelas festival. Harganya murah-murah saja, per lembar tiket dihargai Rp 110 ribu berlaku per hari," kata A. Judiarto, perwakilan promotor MXGP Indonesia yang juga ketua umum PP IMI DKI Jakarta di kantor detikcom, Rabu (22/2/2017). 

Selain bisa menyaksikan tiga kategori balapan itu, pemilik tiket juga dapat melihat langsung aksi freestyle motocross oleh Alex Martin, Alastair James Sarer, dan William Van de Putte. 

"Mereka akan membuat atraksi-atraksi memukau dari awal sampai akhir," tutur Judiarto. 

"Agar tak kehabisan tiket untuk menikmati itu semua, sebaiknya penonton memesan tiket presale yang dibuka sampai 28 Februari," imbuh dia. '''

    print(summarizer(paragraph))