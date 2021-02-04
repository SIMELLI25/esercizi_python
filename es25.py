input("ES 25")
#i voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario 
#che ha per chiave la matricola, mentre il valore associato è il voto. 
#Elenca i risultati in ordine crescente di voto
#e successivamente visualizza quali voti tra loro sono stati assegnati, riducendo a uno i voti assegnati.
count = 1
dict_voti = {}
list_voti = []
dict_altro = {}
while True:
    if count == 31:
        break
    voto = int(input("Inserisci il voto dello studente: "))
    if voto > 10:
        print("Il voto massimo che puoi inserire è 10! riprova.")
        voto = int(input("Inserisci il voto dello studente: "))
    list_voti.append(voto)
    dict_altro[voto] = count
    dict_voti[count] = voto
    count += 1
list_voti.sort()
print("Questo è l'elenco in ordine crescente di voto")
for i in list_voti:
    print("Matricola", dict_altro[i], ":", i)