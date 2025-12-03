"""
01.1.1 Appuntamenti. In un programma di calendarizzazione (scheduling) di eventi, verificare se due 
appuntamenti della stessa giornata si sovrappongono. Per semplicità, ipotizziamo che gli 
appuntamenti inizino sempre a un’ora esatta (senza minuti) e usiamo l’orario militare (cioè con le 
ore che vanno da 0 a 23). Determinare se l’appuntamento che inizia all’ora start1 e termina all’ora 
end1 si sovrappone all’appuntamento che inizia all’ora start2 e termina all’ora end2. Lo 
pseudocodice seguente descrive un possibile algoritmo per determinare una sovrapposizione. 
Se start1 > start2  
s = start1  
Altrimenti  
s = start2  
Se end1 < end2  
e = end1  
Altrimenti  
e = end2  
Se s < e  
Gli appuntamenti si sovrappongono  
Altrimenti  
Gli appuntamenti non si sovrappongono  
 
Seguite passo dopo passo l’esecuzione dello pseudo-codice con gli appuntamenti 10–12 e 11–13, poi 
con gli appuntamenti 10–11 e 12–13; disegnate il diagramma di flusso per l’algoritmo; spiegate il 
funzionamento dell’algoritmo e verificate se esso sia corretto; spiegate il significato delle variabili s 
ed e. [R3.12
"""

start1=int(input("Inserire orario inizio meeting 1: "))
end1=int(input("Inserire orario fine meeting 1: "))
start2=int(input("Inserire orario inizio meeting 2: "))
end2=int(input("Inserire orario fine meeting 2: "))

if start1>start2:
    start=start1
else:
    start=start2

if end1>end2:
    end=end2
else:
    end=end1

if start<end:
    print("Sovrapposizione orario")
else:
    print("Gli orari non si sovrappongono")





