import sys
import codecs
import nltk
from nltk import word_tokenize,sent_tokenize

#questo programma restituisce un'unica lista di token contenente tutti i token del testo

def main(file1):
  fileInput = codecs.open(file1, "r", "utf-8")
  tokensTOT=[]
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
    #concateno la frase appena tokenizzata con le tokenizzazioni precedenti
    tokensTOT = tokensTOT+tokens #l'operatore + concatena i vettori
  #stampo il vettore di tutte le parole
    print ("Tutti i token della frase:")
    print (tokensTOT) 

main(sys.argv[1])
  
