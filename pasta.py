from spalla import Verifica

Verifica.firma("Simone Melli")
#Verifica.stampa_esercizi()
#Verifica.stampa_voto()

'''
es = Verifica.inizia_esercizio(1)
print(es)
print(es.dati)
es.consegna(es.dati.lower())
'''
'''
es = Verifica.inizia_esercizio(2)
print(es)
print(es.dati)
es.consegna(es.dati*es.dati)
'''
'''
es = Verifica.inizia_esercizio(3)
print(es)
print(es.dati)
es.consegna(es.dati["cognome"])
'''
'''
es = Verifica.inizia_esercizio(4)
print(es)
print(es.dati)
es.consegna(len(es.dati))
'''
'''
es = Verifica.inizia_esercizio(5)
print(es)
print(es.dati)
lista = []
for i in es.dati:
    s = i.upper()
    lista.append(s)
es.consegna(lista)
'''
'''
es = Verifica.inizia_esercizio(6)
print(es)
print(es.dati)
es.consegna(sum(es.dati))
'''
'''
es = Verifica.inizia_esercizio(7)
print(es)
print(es.dati)
somma = 0
for i in es.dati:
    if i > 5:
        somma += i
es.consegna(somma)
'''
'''
es = Verifica.inizia_esercizio(8)
print(es)
print(es.dati)
somma = 0
for i in es.dati:
    if es.dati.index(i) % 2 == 0:
        somma += i
es.consegna(somma)
incompleto
'''
'''
es = Verifica.inizia_esercizio(9)
print(es)
print(es.dati)
somma = 0
for i in es.dati:
    if es.dati.index(i) % 2 != 0:
        somma += i
es.consegna(somma)
incompleto
'''
'''
es = Verifica.inizia_esercizio(10)
print(es)
print(es.dati)
es.consegna(es.dati.sort())
incomp0leto
'''
