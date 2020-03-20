# -*- coding: utf-8 -*-

import sys
import codecs
import nltk

def CalcolaLunghezzaEToken(frasi):
    lunghezzaTOT=0.0
    tokensTOT=[]
    for frase in frasi:
        #divido la frase in token
        tokens=nltk.word_tokenize(frase)
        #creo la lista che contiene tutti i token del testo
        tokensTOT=tokensTOT+tokens
    #calcolo la lunghezza
    lunghezzaTOT=len(tokensTOT)
    #restituisco i risultati
    return lunghezzaTOT, tokensTOT

def main(file1):
    freqTokenMax=0
    #leggo il file
    fileInput1=codecs.open(file1, 'r', 'utf-8')
    raw1=fileInput1.read()
    #carico il tokenizzatore di nltk
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    #divido il file in frasi
    frasi1=sent_tokenizer.tokenize(raw1)
    #chiamo la funzione CalcolaLunghezzaEToken sul testo diviso in frasi
    lunghezza1, listaToken=CalcolaLunghezzaEToken(frasi1)
    #calcolo il vocabolario del testo
    vocabolario=set(listaToken)
    #scorro il vocabolario un token per volta
    for i in vocabolario:
        #calcolo la frequenza di ogni token
        freqToken=listaToken.count(i)
        #verifico se il token e' il piu' frequente di quelli gia' osservati
        if freqToken>freqTokenMax:
            freqTokenMax=freqToken
            tokenMax=i
    #stampo i risultati
    print 'il file', file1, "e' lungo", lunghezza1, 'token'
    print "il token piu' frequente e':",  tokenMax, "\tcon frequenza:", freqTokenMax

main (sys.argv[1])
