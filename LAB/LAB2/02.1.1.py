"""
02.1.1 Due numeri. Scrivere un programma che memorizzi due numeri interi in due costanti definite 
nel codice, e poi ne visualizzi:  
A. La somma; 
B. La differenza; 
C. Il prodotto; 
D. Il valore medio; 
E. La distanza (cioè il valore assoluto della differenza); 
F. Il valore massimo (cioè il maggiore tra i due); 
G. Il valore minimo (cioè il minore tra i due). 
Suggerimento: utilizzare le funzioni max() e min() definite in Python. Esse accettano una sequenza 
di valori separati da virgola in input e restituiscono rispettivamente il valore massimo e minimo della 
sequenza (ad esempio, max(10, 5) restituisce 10).


"""
A=10
B=7
somma=A+B
differenza=A-B
prodotto=A*B
media=(A+B)/2
distanza=abs(differenza)
massimo=max(A,B)
minimo=min(A,B)
print(somma,differenza,prodotto,media,distanza,massimo,minimo)