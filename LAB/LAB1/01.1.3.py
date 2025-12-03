"""
01.1.3 Sulla strada. Calcolare la percentuale di utilizzo della vostra automobile per uso personale e, 
separatamente, per recarvi al lavoro. Conoscete la distanza tra casa vostra e il vostro luogo di lavoro 
e, dato un periodo di tempo, avete registrato il valore riportato dal contachilometri all’inizio ed alla 
fine del periodo; inoltre è noto il numero di giorni in cui vi siete recati al lavoro in tale periodo. 
[R1.16]


"""
#calcolo la percentuale di uilizzo dell'automobile
casa_lavoro=25 #km
km_mese=2500
giorni_lavoro=17

km_lavoro=2*casa_lavoro*giorni_lavoro #2 perchè c'è andata e ritorno
km_personali=km_mese-km_lavoro

km_lavoro_percentuali=(km_lavoro/km_mese)*100
km_personali_percentuale=100-km_lavoro_percentuali

print(f"In un mese uso l'auto per uso lavorativo il {km_lavoro_percentuali} delle volte e per uso personale il {km_personali_percentuale}")
