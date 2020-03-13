#Nomor 3b

import re
from collections import Counter

tokenList = []
termFreq = {}
stopList = []

text = open("corpus.txt", encoding="ISO-8859-1").read()
stopWords = open("stopWord.txt","r")
fileOpen = open("token.txt","w", encoding="ISO-8859-1")

for word in stopWords:
    word = word.replace("\n","")
    stopList.append(word)

#menyamakan kapitalisasi kata
# def caseFolding(inputText):
#     lowerCase = inputText.lower()
#     return lowerCase

# def stopWord(inputList):
#     for word in inputList:
#         if word not in stopList:
#             inputList.append(word)
#     return inputList

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
print("Jumlah Dokumen :", jumlah, "\n")

#3b
counter = 0
print("20 kata dengan frekuensi tertinggi")
for w in sorted(termFreq, key=termFreq.get, reverse=True):
    print(w, termFreq[w])
    counter += 1
    if counter == 20:
        break
print()

#3f
countKata = 0
for word in termFreq.keys():
    if termFreq[word] < 10:
        countKata += 1
print("Jumlah kata yang frekuensinya kurang dari 10 :", countKata, "\n")

#3g
print("Jumlah kata :", len(tokenList), "\n")

#3h
print("Jumlah kata unik :", len(termFreq), "\n")
