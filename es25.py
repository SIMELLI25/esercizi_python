input("ES 25")
#i voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario 
#che ha per chiave la matricola, mentre il valore associato è il voto. 
#Elenca i risultati in ordine crescente di voto
#e successivamente visualizza quali voti tra loro sono stati assegnati, riducendo a uno i voti assegnati.
count = 1
dict_voti = {}
while True:
    if count == 6:
        break
    print("Inserisci il voto della matricola", count)
    voto = int(input("Voto: "))
    if voto > 10:
        print("Il voto massimo che puoi inserire è 10! riprova.")
        voto = int(input("Voto: "))
    dict_voti[count] = voto
    count += 1
list_voti = list(dict_voti.values())
list_voti.sort()
print("Questo è l'elenco in ordine crescente di voto")
for i in list_voti:
    print("Voto", i)
list_voti = []
for i in dict_voti:
    if dict_voti[i] not in list_voti:
        list_voti.append(dict_voti[i])
print("I voti assegnati sono i seguenti: ")
for i in list_voti:
    print(i)