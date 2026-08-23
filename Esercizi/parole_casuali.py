""" stampare 10 parole casuali di lunghezza compresa tra 5 e 10 lettere ciascuna"""

import random
# random è una libreria di funzioni pseudo-randomiche
# esempio random.randint(a,b)- Genera un intero casuale compreso tra a e b
# esempio random.random() - Genera un float random tra 0 e 1 

# Ripeto 10 volte un operazione

volte=0
while volte<10: 

    # costruisci una stringa random
    # costruisci una stringa di lunghezza casuale
    lunghezza=random.randint(5,10) # mi sceglie una lunghezza random della parola
    s="" # l'accumulatore è una stringa che accumula caratteri
    while len(s)<lunghezza:
        alfabeto="abcdefghijklmnopqrstuvwxyz"
        posizione_lettera=random.randint(1,len(alfabeto))
        lettera=alfabeto[posizione_lettera-1]
        s+=lettera
        
        
    print(s)
    volte+=1

    # scegli un singolo carattere casualmente
    # scelgo un numero tra 0 e 25 lettere alfabeto
    #scelgo la lettera dell'alfabeto in tale posizione

"""alfabeto="abcdefghijklmnopqrstuvwxyz"
posizione_lettera=random.randint(0,len(alfabeto))
lettera=alfabeto[posizione_lettera]
print(lettera)"""