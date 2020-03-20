import sys
import codecs #permette di gestire un file con diverse codifiche

def main(file1): #definisco la funzione main
  fileInput = codecs.open(file1, "r", "utf-8") #open e' un metodo della classe codecs
  var = fileInput.read() #il metodo read legge unfile e assegna tutto il suo contenuto alla variabile var di tipo String 
  varS = var.split()
  for parola in varS:
    print ("Parola:", parola.encode("utf-8")) #metodo encode trasforma una stringa dal formato interno usato da python nel formato scelto

main(sys.argv[1]) #parametro = file di testo
