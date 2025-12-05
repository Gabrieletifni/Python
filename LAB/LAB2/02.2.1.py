"""
02.2.1 Caratteri. Scrivere un programma che memorizzi una stringa in una variabile e, a partire da 
quella variabile, visualizzi i primi tre caratteri della stringa, seguiti da tre punti, ancora seguiti dagli 
ultimi tre caratteri. Ad esempio, se la stringa viene inizializzata al valore “Mississippi”, il 
programma deve visualizzare “Mis...ppi”. Cosa succede della stringa è più corta di 6 caratteri? E 
se è più breve di 3 caratteri?

"""
nome=str(input("Inserire nome: "))
lunghezza=len(nome)
if lunghezza==6:
    print("Non vedrò puntini in mezzo dato che la stringa è esattamente lunga 6 caratteri")
if lunghezza<6:
    print("La stringa è più corta di 6 lettere")
    
if lunghezza>6: 
 primi_3=nome[:3]
 ultimi_3=nome[-3]+nome[-2]+nome[-1]
 puntini=lunghezza-6
 nuovo=primi_3+(puntini*".")+ultimi_3
 print(nuovo)
