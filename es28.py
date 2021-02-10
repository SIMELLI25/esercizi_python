#I nomi delle città e i Corrispondenti codici di Avviamento Postale (CAP) vengono inseriti da tastiera
#e memorizzati in un dizionario, dove il CAP è la chiave.
#Fornito poi da tastiera il nome di una città, costruisci un programma che visualizzi il suo CAP 
#oppure un messaggio nel caso la città non sia compresa nell'elenco.
#Analogamente, fornedo il CAP restituisce il nome della città oppure un messaggio di errore.
from os import system
dict_city = {}
dict_cap = {}
count = 0
n_city = int(input("Quante città vuoi inserire nell'elenco? "))
while True:
    if count == n_city:
        break
    city = input("Inserisci il nome della città: ")
    cap = int(input("Inserisci il CAP della città: "))
    dict_city[cap] = city
    dict_cap[city] = cap
    count += 1
system("cls")
print("Dato il CAP o la città, vuoi sapere rispettivamente la città o il CAP?")
print("Digita 1 se vuoi sapere la città")
print("Digita 2 se vuoi sapere il CAP")
cap_or_city = int(input("Risposta: "))
if cap_or_city == 1:
    cap = int(input("Inserisci il CAP: "))
    if cap in dict_city:
        city = dict_city[cap]
        print("La città avente come CAP", cap, "è", city)
    else:
        print("Nessuna città avente come CAP", cap, "riconosciuta")
elif cap_or_city == 2:
    city = input("Inserisci il nome della città: ")
    if city in dict_cap:
        cap = dict_cap[city]
        print("Il CAP della città", city, "è", cap)
    else:
        print("Nessun CAP della città", city, "riconosciuto")