"""  
03.2.1 Andamenti. Scrivere un programma che legga tre numeri e visualizzi il messaggio “increasing” 
se sono in ordine strettamente crescente, “decreasing” se sono in ordine strettamente decrescente 
e “neither” se non sono né in ordine crescente né in ordine decrescente. “Strettamente crescente” 
significa che ciascun valore deve essere maggiore del precedente (analogo significato ha il termine 
decrescente): la sequenza 3 4 4, quindi, non va considerata crescente.


"""

primo=float(input("Inserire primo numero: "))
secondo=float(input("Inserire secondo numero: "))
terzo=float(input("Inserire terzo numero: "))

if terzo>secondo and secondo>primo:
    print("Strettamente crescente")
elif primo>secondo and secondo>terzo:
    print("Strettamente decrescente")
else:
    print("neither increasing or decreasing")