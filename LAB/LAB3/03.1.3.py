"""  
03.1.3 Stringhe e sottostringhe. Le sequenze di DNA sono come lunghe stringhe composte da solo 
quattro lettere: 'A', 'C', 'T' e 'G'. Scrivere un programma che prende in input una “sequenza 
lunga” di DNA di venti caratteri e una “sequenza breve” di tre caratteri e visualizza:  
I. se la “sequenza lunga” contiene la “sequenza breve”; 
II. se presente, a partire da quale posizione della “sequenza lunga” è presente la “sequenza 
breve”; 
III. se presente, quante volte la sequenza “lunga” contiene la sottostringa più breve

"""
DNA=['A','C','T','G']
sequenza_lunga=input("Inserire una sequenza di venti caratteri tra A,C,T,G:")
sequenza_breve=input("Inserire una sequenza breve di tre caratteri tra A,C,T,G: ")
#INIZIO CONTROLLI
if len(sequenza_lunga)!=20:
   print("Hai inserito una lunghezza della sequenza lunga errata")
elif len(sequenza_breve)!=3:
   print("Hai inserito una lunghezza della sequenza breve errata")
   
flag1=False #lettere sequenza lunga
flag2=False #lettere sequenza breve
for lettera in sequenza_lunga:
    if lettera not in DNA:
        flag1=True
        

for lettera in sequenza_breve:
    if lettera not in DNA:
        flag2=True
        
if flag1==True:
 print("Nella sequenzalunga hai inserito una lettera non corretta!")
elif flag2==True:
 print("Nella sequenza breve hai inserito una lettera non corretta!")

contenuta=False
if sequenza_breve in sequenza_lunga:
   contenuta=True

if contenuta==True:
   indice=sequenza_lunga.find(sequenza_breve)
   print(f"La sequenza breve inizia la prima volta in posizione {indice} della sequenza lunga")
   ricorrenze=sequenza_lunga.count(sequenza_breve)
   print(f"La sequenza breve è contenuta {ricorrenze} volte nella sequenza lunga")
else:
   print("La sequenza breve non è contenuta nella sequenza lunga")