"""
01.1.4 Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche. Per 
ragioni estetiche l’architetto ha specificato che la prima e l’ultimapiastrella 
devono essere nere. Il vostro compito è calcolare il numero di piastrelle 
necessarie e il vuoto a ciascuna delle due estremità della riga, dato lo spazio
disponibile e la larghezza di ogni piastrella.
"""
muro=100
piastrella=3

coppie=(muro-piastrella)//(2*piastrella)
numero_piastrelle=2*coppie+1
spazio=(muro-numero_piastrelle*piastrella)/2
print(f"ci sono {coppie} coppie di BN e lo spazio lasciato è {spazio}")