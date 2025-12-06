"""  
02.1.5 Forza elettrica. Secondo la legge di Coulomb, la forza elettrica (espressa in Newton) tra due 
particelle cariche con carica, rispettivamente, Q1 e Q2, separate da una distanza r, è  
𝐹 =  𝑄1 𝑄2
4 𝜋 𝜀 𝑟2 
dove 𝜀 = 8.854 × 10−12 Farad / metro. Scrivere un programma che calcoli e mostri a video la 
forza relativa ad una coppia di particelle cariche, permettendo all’utente di scegliere i valori Q1, Q2 
(in Coulomb) e r (in metri).

"""
from math import *

epsilon=8.844*10**(-12)
Q1=float(input("Inserire il valore della prima carica: "))
Q2=float(input("Inserire il valore della seconda carica: "))
r=float(input("Inserire il valore della distanza tra le due particelle:"))

#calcolo della forza elettrica
F=(Q1*Q2)/(4*pi*epsilon*(r**2))
print(f"Il valore dell forza elettrica è {F:10.2f} Netwon")