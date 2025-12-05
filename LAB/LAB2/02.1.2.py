"""
Scrivere un programma che, a partire dalle resistenze dei tre resistori, immesse in input dall’utente, 
calcoli la resistenza totale, utilizzando la legge di Ohm
"""
#R2 ed R3 sono in parallelo da figura esercizio
#R1 è in serie al parallelo delle prime 2

R1=10
R2=4
R3=5

parallelo=(R2*R3)/(R2+R3)
serie=R1+parallelo
print(f"La resistenza totale vale circa {round(serie)} ohm")