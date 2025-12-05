"""
02.2.5 Immatricolazioni. La matricola degli studenti di un Ateneo è composta da due parti: una 
lettera e una sequenza di numeri. Scrivere un programma che, a partire da due codici di matricola, li 
mostri a schermo in ordine crescente in base alla sola parte numerica. Suggerimento: utilizzare le 
funzioni predefinite del linguaggio Python.

"""

matricola1="s246801"
matricola2="s347470"

numero_matricola1=matricola1[1:]
numero_matricola2=matricola2[1:]
massimo=max(numero_matricola1,numero_matricola2)
minimo=min(numero_matricola1,numero_matricola2)

print(f"Le matricole in ordine crescente sono {minimo,massimo}")