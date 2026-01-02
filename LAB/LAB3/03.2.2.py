"""  
03.2.2 Voti. Scrivere un programma che traduca un voto in lettere inserito dall’utente nel 
corrispondente voto numerico e lo stampi. I voti in lettere sono 'A', 'B', 'C', 'D' e 'F', 
eventualmente seguiti da un segno + o –. I loro valori numerici sono, nell’ordine, 4.0, 3.0, 2.0, 
1.0 e 0.0. I voti 'F+' e 'F–' non esistono. Un segno + aumenta il voto numerico di 0.3, mentre 
un segno – lo diminuisce della stessa quantità. Il voto 'A+' è comunque uguale a 4.0.

"""
valore=0
voto=0
votofinale=0
flag_segno=False
from string import *
voto_lettere=input("Inserire voto in lettere: ")
if voto_lettere=='A+':
    votofinale=4.0

lettera=voto_lettere[0]
if len(voto_lettere)>1:
    flag_segno=True
    segno=voto_lettere[1]
    if segno=='+':
        valore=0.3
    elif segno=='-':
        valore=-0.3

if lettera=='B':
    voto=3.0
elif lettera=='C':
    voto=2.0
elif lettera=='D':
    voto=1.0
else:
    voto=0.0

if flag_segno and voto_lettere!='A+':
     if segno=='-':
      votofinale=voto+valore
     else:
        votofinale=voto+valore
else:
    votofinale=voto


print(f"Il voto finale è {votofinale}")

