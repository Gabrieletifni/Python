"""
NBN
immagino 3 piastrelle
spazio=lunghezza_muro-lunghezzatot_piastrelle
il rimanente spazio deve essere diviso sui 2 lati
il valore dello spazio per lato deve essere minore della larghezza di una piastrella
print(120/25)  mi da 4.8, divisione corretta
print(120//25) mi da 4, cioè la divisione intera 
n.b:IO voglio arrotondare la divisione al valore dispari, dato che devo iniziare e finire con una nera
"""
from math import *

MURO=120
PIASTRELLA=25
x=MURO/PIASTRELLA #numero di piastrelle se non ci fossero vincoli, con anche parte frazionaria

n_piastrelle_totali= int(x)-(1-int(x)%2) #se il resto di muro/piastrella è 1 vuol dire che il risultato era dispari
#la formula sopra, se il risultato di x è pari me lo abbassa di 1, se è dispari lo lascia uguale
#questo mi serve per capire quante piastrelle mettere (di sicuro un numero dispari) 
print(n_piastrelle_totali )
n_bianche=(n_piastrelle_totali-1)//2
n_nere=n_piastrelle_totali-n_bianche

print("Nere:",n_nere)
print("Bianche:",n_bianche)

#devo ancora calcolare lo spazio vuoto
vuoto=(MURO-(n_piastrelle_totali*PIASTRELLA))/2
print("Spazio vuoto:",vuoto)


#--------------------------------
"""Altro ragionamento
coppiebn=(muro-piastrella)/(2*piastrella)  metto una nera e poi nello spazio che rimane guardo quante coppie b-n rimangono (mi darà il numero di bianche)

"""
