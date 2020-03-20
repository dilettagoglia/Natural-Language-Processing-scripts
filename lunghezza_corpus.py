# -*- coding: utf-8 -*-

import sys
import codecs
import nltk
from nltk import word_tokenize,sent_tokenize

def CalcolaLunghezza(frasi):
    lunghezzaTOT=0.0
    tokensTOT=[]
    for frase in frasi:
        #divido la frase in token
        tokens=nltk.word_tokenize(frase)
        #calcolo la lunghezza
        tokensTOT=tokensTOT+tokens
    lunghezzaTOT=len(tokensTOT)
    #restituisco il risultato
    return lunghezzaTOT

def main(file1):
    #leggo il file
    fileInput1=codecs.open(file1, 'r', 'utf-8')
    raw1=fileInput1.read()
    #carico il tokenizzatore di nltk
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    #divido il file in frasi
    frasi1=sent_tokenizer.tokenize(raw1)
    #chiamo la funzione CalcolaLunghezza sul testo diviso in frasi
    lunghezza1=CalcolaLunghezza(frasi1)
    #stampo i risultati
    print ('Il file', file1, "e' lungo", lunghezza1,' token')

main(sys.argv[1])
