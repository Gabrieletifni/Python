''' Dato un valore T inserito da utente, quanti quadrati dei numeri
interi bisogna sommare per fare si che la somma sia>T?

'''

T=int(input("Inserisci il totale: "))
i=0
somma=0
numero=1
while somma<T:
    quadrato=numero*numero
    somma+=quadrato
    numero+=1
    i+=1
    print(i,somma)

print(f'Ci vogliono {i} quadrati per raggiungere T')