"""Si realizzi un programma che determini il vincitore di una mano di carte a briscola:
il programma riceve:
- info sul seme di briscola (CUORI,FIORI,QUADRI,PICCHE)
- la prima carta giocata
- la seconda carta giocata

e deve visualizzare in uscita il messaggio "vince la prima carta" se la prima carta vince, oppure "vince la seconda carta" se la seconda carta vince.

Il valore delle carte è il seguente:
- Asso: 11 punti
- Tre: 10 punti
- J,Q,K valgono rispettivamente 2,3,4 punti
- Tutte le altre carte (2,4,5,6,7) valgono 0 punti e differiscono solo perchè la carta con valore maggiore vince sulla carta con valore minore.

Secondo le regole del gioco, la carta vincente si determina nel seguente modo:
- Se una delle due carte è di briscola e l'altra no, vince la carta di briscola.
- Se entrambe le carte sono di briscola, vince quella con il valore maggiore.
- Se nessuna delle due carte è di briscola, vince sempre la prima carta giocata.

L'informazione sulla carta giocata è fornita come stringa di 2 caratteri: il primo carattere rappresenta il valore della carta (uno di "A", "2", "3", "4", "5", "6", "7", "J", "Q", "K") e il secondo carattere rappresenta il seme della carta (uno di "CUORI", "FIORI", "QUADRI", "PICCHE").


"""

# Lettura dei dati in ingresso (input)
briscola=input("Inserisci il seme di briscola: ") #C,Q,F,P
if briscola not in {'J','Q','C','F'}:
    print('Seme non valido')
    briscola=input("Inserisci il seme di briscola: ")
carta1=input("Carta primo giocatore: ")
carta2=input("Carta secondo giocatore: ")

# Verificare la correttezza dei dati in ingresso



#Una carta con il seme di briscola vince sempre su una carta di seme diverso
# caso1: Carta1 è di briscola, Carta2 no--vince 1
seme1=carta1[1]
seme2=carta2[1]
valore1=carta1[0]
valore2=carta2[0]

ordine_crescente='24567JQK3A'  #metto i valori possibili in ordine crescente di punteggio
# le posizioni di indici maggiori corrispondono a carte di valore maggiore
ordine1=ordine_crescente.find(valore1)
ordine2=ordine_crescente.find(valore2)

if seme1==briscola and seme2!=briscola:
    print(f'Vince: {carta1}')
elif seme2==briscola and seme1!=briscola: #con elif non entro nella condizione se il primo if era vero
    print(f'Vince: {carta2}')
elif seme1!=seme2:
    print(f'Vince {carta1}') #sono nell'elif quindi nel caso diverso dai precedenti, cioè nessuno dei 2 semi è una briscola ed i semi delle 2 carte sono diversi tra di loro
else: #Ora inizio a considerare anche i casi in cui devo considerare il valore della carta, perchè tutti e due i semi ora sono UGUALI ( di briscola o non di briscola )
    if ordine1>ordine2: #rimane il problema che i valori devono essere considerati per il loro punteggio, quindi un 3 vale di più di un J 
        print(f'Vince: {carta1}')
    else:
        print(f'Vince: {carta2}')
