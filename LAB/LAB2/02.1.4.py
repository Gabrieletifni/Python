"""
02.1.4 Auto ibrida. Scrivere lo pseudocodice e il relativo programma Python che aiuta una persona a 
decidere se comprare o meno un’auto ibrida. Gli input del programma dovrebbero essere: 
I. il costo di un’auto nuova; 
II. la stima dei chilometri percorsi in un anno; 
III. La stima del costo del carburante; 
IV. L’efficienza in chilometri al litro; 
V. La stima del valore di rivendita dell’auto usata dopo 5 anni. 
Calcolare il costo totale di proprietà dell’auto per 5 anni (per semplicità, non tenere in 
considerazione il costo di finanziamenti). Per fornire gli input al programma, ricercare sul Web prezzi 
e consumi realistici per due alternative per l’acquisto di un’auto nuova nella stessa fascia di prezzo: 
un modello ibrido e uno a benzina. Eseguire il programma due volte per comparare le due 
alternative, considerando l’attuale prezzo del carburante e la previsione di percorrere 30’000 
chilometri all’anno. 

"""
costo_nuovo=int(input("Inserisci costo auto nuova: "))
km_annui=int(input("Inserisci il numero di km annui: "))
carb=float(input("Inserire il costo del carburante: "))
eff=int(input("Inserire l'efficienza in km al litro: "))
rivendita=int(input("Inserisci il prezzo di rivendita: "))

costo_totale=costo_nuovo+(km_annui/eff)*carb-rivendita
print(f"Il costo totale di auto è: {costo_totale} €")