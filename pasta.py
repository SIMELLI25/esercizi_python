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
    if i % 2 != 0:
        somma += i
es.consegna(somma)
'''
'''
es = Verifica.inizia_esercizio(10)
print(es)
print(es.dati)
es.consegna(sorted(es.dati))
'''
'''
es = Verifica.inizia_esercizio(11)
print(es)
print(es.dati)
lista = []
for i in es.dati:
    e = i.lower()
    lista.append(e)
es.consegna(sorted(lista))
'''
'''
es = Verifica.inizia_esercizio(12)
print(es)
print(es.dati)
lista = []
for i in es.dati:
    e = i-1
    lista.append(e)
es.consegna(lista)
'''
'''
es = Verifica.inizia_esercizio(13)
print(es)
print(es.dati)
lista = []
for i in es.dati:
    if es.dati[i] == len(es.dati)-1:
        e = i
    else:
        e = i + es.dati[es.dati.index(i)+1]
    lista.append(e)
print(lista)
incompleto
'''

'''
es = Verifica.inizia_esercizio(14)
print(es)
print(es.dati)
diz = {}
count_zeri = 0
count_pos = 0
count_neg = 0
for i in es.dati:
    if i == 0:
        count_zeri += 1
    elif i > 0:
        count_pos += 1
    elif i < 0:
        count_neg += 1
diz["zeri"] = count_zeri
diz["positivi"] = count_pos
diz["negativi"] = count_neg
es.consegna(diz)
'''
