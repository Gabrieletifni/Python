# Stampa i quadrati di tutti i numeri che l'utente inserisce da tastiera, fino a quando l'utente non inserisce il valore '*'
'''
risposta=input("Numero: ")
while risposta!="*":
    numero=int(risposta)
    quadrato=numero*numero
    print(numero,quadrato)

    risposta=input("Numero:")

print("Fine")
'''
#Leggere un valore intero da utente, nel caso in ci non sia un numero intero, chiedere di reinserire il valore

risposta_utente=input("Numero:")
while not risposta_utente.isnumeric(): # Si entra nel ciclo solo se il valore risposta_utente NON è un numero.
  print("Valore non valido")
  risposta_utente=input("Numero:")

numero_intero=int(risposta_utente)
print(numero_intero)



