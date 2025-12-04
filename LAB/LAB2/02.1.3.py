"""
02.1.3 Cifre. Scrivere un programma che memorizzi in una costante un numero intero positivo di 
cinque cifre (quindi compreso tra 10000 e 99999), e visualizzi le singole cifre di cui è composto. Ad 
esempio, avendo il numero 16384, il programma deve visualizzare, su righe separate: 1 6 3 8 4.

"""
VALORE=21963
#lo converto in stringa???
valore=str(VALORE)
for i in range(len(valore)):
    print(valore[i])