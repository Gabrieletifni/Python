"""
01.1.2 Stagioni. L’algoritmo seguente individua la stagione (Spring, Summer, Fall o Winter, cioè, 
rispettivamente, primavera, estate, autunno o inverno) a cui appartiene una data, fornita come 
mese e giorno.  
Se mese è 1, 2 o 3 
stagione = “Winter”  
Altrimenti se mese è 4, 5 o 6 
stagione = “Spring”  
Altrimenti se mese è 7, 8 o 9 
stagione = “Summer”  
Altrimenti se mese è 10, 11 o 12 
stagione = “Fall”  
Se mese è divisibile per 3 e giorno >= 21  
Se stagione è “Winter” 
stagione = “Spring”  
Altrimenti se stagione è “Spring” 
stagione = “Summer”  
Altrimenti se stagione è “Summer” 
stagione = “Fall”  
Altrimenti 
stagione = “Winter”   
 
Disegnate il diagramma di flusso per l’algoritmo. Verificate se l’algoritmo si comporta correttamente 
con una serie di date di prova. [R3.13]
"""

mese=int(input("Inserire mese: "))
winter=[1,2,3]
spring=[4,5,6]
summer=[7,8,9]
fall=[10,11,12]
if mese in winter:
    print(f"il mese {mese} è in inverno")
elif mese in spring:
    print(f"il mese {mese} è in primavera")
elif mese in summer:
    print(f"il mese {mese} è in estate")
elif mese in fall:
    print(f"il mese {mese} è in autunno")
else:
    print(f"il mese {mese} non appartiene al calendario")




