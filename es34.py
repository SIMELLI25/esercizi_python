input("ES 34")
#Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo. Scrivi un programma che comprenda due funzionalità
#- L'operazione per registrare i dati dei partecipanti;
#- L'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: 
#  si tratta dei nomi dell'elenco, eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco.
#  La funzione che produce l'elenco deve anche aggiornare l'elenco dei partecipanti ai quali è già stata inviata la lettera
dict_part_orar = {}
list_orari = []
dict_def = {}
list_cas = [] # lista per eliminare gli elementi dal dizionario
while True:
    print("Se i partecipanti sono terminati, inserisci STOP")
    partecipante = input("Inserisci il nome del partecipante: ")
    if partecipante == "STOP":
        break
    orario = input("Inserisci l'orario di arrivo: ")
    dict_part_orar[orario] = partecipante
    list_orari.append(orario)
list_orari.sort() # metto in ordine crescente gli orari di entrata
for i in list_orari:
    dict_def[i] = dict_part_orar[i]
print("Elenco in ordine di arrivo:")
for j in dict_def:
    print("ore", j, ":", dict_def[j])
for d in dict_def:
    print(dict_def[d], "entrato alle ore", d)
    conferma = input("La letterea di conferma è già stata inviata? ")
    if conferma == "si" or conferma == "SI":
        list_cas.append(d)
for q in list_cas:
    del dict_def[q] # elimino dal dizionario dict_def chi ha già avuto la lettera di conferma
print("I partecipanti ai quali va data la lettera di conferma sono i seguenti: ")
for u in dict_def:
    print(dict_def[u])