import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import special

tokenList = []
termFreq = {}
zipF = {}
stopList = []
stemLib = []

text = open("corpus.txt", encoding="ISO-8859-1").read()
stopWords = open("stopWord.txt","r")
fileOpen = open("token.txt","w", encoding="ISO-8859-1")
docToken = open("docToken.txt","w", encoding="ISO-8859-1")
stemLibrary = open("stemLibrary.txt", encoding="cp1252").read()

for word in stemLibrary:
    stemLib.append(word)

for word in stopWords:
    word = word.replace("\n","")
    stopList.append(word)

#mengambil kalimat didalam tag <TITLE> dan <TEXT> pada seluruh corpus
docTokens = re.split('<DOC>', text)
for docs in docTokens:
    doc = docs.replace("-"," ")
    doc = re.split('<[^>]*>|\n\t|\n|\d{15}|[A-Z]{0,3}\-\d|\s|\,|\.|"|\\x94|\\x93|\d|\/|\(|\)|\!|\@|\#|\%|\?|\[|\]', doc)
    for word in doc:
        if word != '' and len(word) > 2:
            docToken.write(word + " ")
    docToken.write("\n")

def preProcessing(inputText, inputList):

    #case folding untuk menyamakan kapitalisasi teks
    inputText = inputText.lower()

    #mengganti karakter "-" dengan " " agar kata berulangan dapat menjadi 2 kata
    inputText = inputText.replace("-"," ")
    token = re.split('<[^>]*>|\n\t|\n|\d{15}|[a-z]{0,3}\-\d|\s|\,|\.|"|\\x94|\\x93|\d|\/|\(|\)|\!|\@|\#|\%|\?|\[|\]', inputText)
 
    for i in token:
        if len(i) > 3:
            #menghilangkan kata-kata yang termasuk stopword
            if i not in stopList:
                inputList.append(i)
    return inputList

#mencari jumlah kata dengan awalan "ber-"
def awalanBer(dictTerm):
    counterBer = 0
    for word in dictTerm.keys():
        if "ber" in word:
            newWord = word.split("ber")
            if newWord[1] in stemLibrary and newWord[0] == '':
                if len(newWord[1]) > 3:
                    # print(word, newWord[1])
                    counterBer += 1
    return counterBer

#mencari jumlah kata dengan akhiran "-kan"
def akhiranKan(dictTerm):
    counterKan = 0
    for word in termFreq.keys():
        if "kan" in word:
            newWord = word.split("kan")
            if newWord[0] in stemLibrary and newWord[1] == '':
                if len(newWord[0]) > 3:
                    # print(word, newWord[0])
                    counterKan += 1
    return counterKan

tokenList = preProcessing(text,tokenList)

#menunliskan token kedalam file token.txt
for word in tokenList:
    fileOpen.write(word + "\n")

#membuat dictionary berisikan term frequency
for word in tokenList:
    if word not in termFreq.keys():
        termFreq[word] = 1
    else:
        termFreq[word] += 1

#3a
doc  = re.findall('<DOC>',text)
jumlah = len(doc)
print("a.) Jumlah Dokumen :", jumlah, "\n")

#3b
counter = 0
print("b.) 20 kata dengan frekuensi tertinggi")
for w in sorted(termFreq, key=termFreq.get, reverse=True):
    print("\t", w, termFreq[w])
    counter += 1
    if counter == 20:
        break
print()

#3e
counter = 0
#mengambil 100 term pertama dengan nilai terbesar
for w in sorted(termFreq, key=termFreq.get, reverse=True):
    # print(w, termFreq[w])
    zipF[w] = termFreq[w]
    counter += 1
    if counter == 100:
        break
#hanya menggunakan 100 term pertama dari dict termFreq, karena memerlukan waktu eksekusi yang sangat lama jika ditampilkan semua sebanyak 21710 term
plt.title("Zipf distribution")
x, y = zip(*zipF.items())
plt.xlabel("Token frequency rank")
plt.ylabel("Absolute fequency token")
plt.plot(x, y)
plt.xticks(rotation='vertical')
print("e.) Menampilkan diagram distribusi zipf\n")

#3f
countKata = 0
for word in termFreq.keys():
    if termFreq[word] < 10:
        countKata += 1
print("f.) Jumlah kata yang frekuensinya kurang dari 10 :", countKata, "\n")

#3g
print("g.) Jumlah kata :", len(tokenList), "\n")

#3h
print("h.) Jumlah kata unik :", len(termFreq), "\n")

#3i
print("i.) Jumlah kata berawalan 'ber-' :", awalanBer(termFreq), "\n")

#3j
print("j.) Jumlah kata berakhiran '-kan' :", akhiranKan(termFreq), "\n")

#3k
sent = re.findall('[\.!?]\W|', text)
print("k.) Jumlah kalimat dalam korpus :", len(sent))
print("\tMenghitung jumlah kalimat didalam korpus dilakukan dengan menggunakan regex untuk mencari banyaknya tag TITLE dan banyaknya tanda baca titik(.), seru(!), tanya(?) yang diikutin dengan whitespace(spasi atau enter)")

plt.show()