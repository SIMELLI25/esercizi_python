#I nomi delle città e i Corrispondenti codici di Avviamento Postale (CAP) vengono inseriti da tastiera
#e memorizzati in un dizionario, dove il CAP è la chiave.
#Fornito poi da tastiera il nome di una città, costruisci un programma che visualizzi il suo CAP 
#oppure un messaggio nel caso la città non sia compresa nell'elenco.
#Analogamente, fornedo il CAP restituisce il nome della città oppure un messaggio di errore.
from os import system
dict_cap = {}
dict_inv = {}
count = 0
n_city = int(input("Quante città vuoi inserire nell'elenco? "))
while True:
    if count == n_city:
        break
    city = input("Inserisci il nome della città: ")
    cap = int(input("Inserisci il CAP della città: "))
    dict_cap[cap] = city
    dict_inv[city] = cap
    count += 1
system("cls")
cap_or_city = input("Dato il CAP o la città, vuoi sapere rispettivamente la città o il CAP?")