# -*- coding: utf-8 -*-

import sys
import codecs
import nltk
from nltk import word_tokenize,sent_tokenize

#questo programma restituisce liste contenenti i token di una frase

def main(file1):
  fileInput = codecs.open(file1, "r", "utf-8")
  var = fileInput.read()
  #carico il modello statistico utilizzato dalla funzione tokenize
  sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
  #divido il testo in frasi con la funzione tokenize(String)
  frasi = sent_tokenizer.tokenize(var) 
  #stampo il testo frase per frase
  for frase in frasi:
    #stampo la frase 
    print ("Frase:", frase.encode("utf-8"))
    #divido la frase in token
    tokens = nltk.word_tokenize(frase) #prende in input una stringa e restituisce una lista di stringhe
    #stampo il vettore delle parole
    print (tokens)
    #stampo le parole
    print ("Parole:")
    for i in tokens:
      print (i.encode("utf-8"))

main(sys.argv[1])
  
