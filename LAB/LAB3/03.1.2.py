"""  
03.1.2 Identikit della stringa. Scrivere un programma che legga una stringa e visualizzi i messaggi 
appropriati, dopo aver verificato se:  
I. contiene soltanto lettere; 
II. contiene soltanto lettere maiuscole;  
III. contiene soltanto lettere minuscole; 
IV. contiene soltanto cifre numeriche decimali; 
V. contiene soltanto lettere e cifre;  
VI. inizia con una lettera maiuscola; 
VII. termina con un punto. 
[P3.17] 


"""
from string import *
parola=input("Inserire una parola: ")
if parola.isalpha():
    print(f"La parola {parola} contiene solo lettere")
else:
    print(f"La parola {parola} non contiene solo lettere")
if parola.isalpha() and parola.isupper():
    print(f"La parola {parola} contiene solo lettere maiuscole")
if parola.isalpha() and parola.islower():
    print(f"La parola {parola} contiene solo lettere minuscole")
if parola.isdigit():
    print(f"La parola {parola} contiene solo numeri")
if parola.isalnum():
    print(f"La parola {parola} contiene cifre e lettere")
prima_lettera=parola[0]
if  prima_lettera.isupper():
    print(f"La parola {parola} inizia con una lettera maiuscola")

if parola.endswith("."):
    print(f"La parola {parola} termina con un punto")
