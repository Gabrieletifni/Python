""" 
01.2.6 Il saldo di un conto bancario dopo il primo, secondo e terzo anno. Il conto ha un saldo iniziale 
di 1000 dollari e vi vengono accreditati interessi annuali al 5%. 

"""
Saldo_iniziale=10000
interesse=0.05
i=0
saldototale=Saldo_iniziale
while i<3:
    saldototale=saldototale+saldototale*interesse
    print(f"Il saldo totale dopo il {i} anno vale {saldototale}")
    i+=1