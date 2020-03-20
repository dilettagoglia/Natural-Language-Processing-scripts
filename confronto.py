# -*- coding: utf-8 -*-
import sys
import codecs
import nltk
from nltk import word_tokenize,sent_tokenize

def CalcolaLunghezza(frasi):
    lunghezzaTOT=0.0
    for frase in frasi:
        #divido la frase in token
        tokens=nltk.word_tokenize(frase)
        #calcolo la lunghezza
        lunghezzaTOT=lunghezzaTOT+len(tokens)
    #restituisco il risultato
    return lunghezzaTOT

def main(file1, file2):
    fileInput1 = codecs.open(file1, "r", "utf-8")
    fileInput2 = codecs.open(file2, "r", "utf-8")
    var1 = fileInput1.read()
    var2 = fileInput2.read()
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    #divido i due file in frasi
    frasi1 = sent_tokenizer.tokenize(var1)
    frasi2 = sent_tokenizer.tokenize(var2)
    lunghezza1 = CalcolaLunghezza(frasi1)
    lunghezza2 = CalcolaLunghezza(frasi2)

    #stampo i risultati
    print ("Il file", file1, "e' lungo", lunghezza1, "token")
    print ("Il file", file2, "e' lungo", lunghezza2, "token")
    if (lunghezza1>lunghezza2):
        print (file1, "e' piu' lungo di", file2)
    elif (lunghezza1<lunghezza2):
        print (file2, "e' piu' lungo di", file1)
    else:
        print ("i due file hanno la stessa lunghezza")

main(sys.argv[1], sys.argv[2])
