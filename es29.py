input("ES 29")
#Tabella delle aliquote:
#fino a 15.000 euro, aliquota 23%
#da 15.001 a 28.000 euro, aliquota 27%
#da 28.001 a 55.000 euro, aliquota 38%
#da 55.001 a 75.000 euro, aliquota 41%
#oltre 75.000 euro, aliquota 43%
#Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e la tassazione media.
list_limiti = [15000, 28000, 55000, 75000, 1000000000000]
list_aliquota = [23, 27, 38, 41, 43]
dict_redd = {}
reddito = int(input("Inserisci il tuo reddito: "))
imposta = 0
for i in range(len(list_limiti)):
    if i == 0:
        tassazione = list_aliquota[i]*list_limiti[i]/100
    else:
        tassazione = list_aliquota[i]*(list_limiti[i]-list_limiti[i-1])/100
    imposta += tassazione
    if reddito > list_limiti[i] and reddito <= list_limiti[i+1]:
        reddito -= list_limiti[i]
        tassazione = reddito*list_aliquota[i+1]/100
        imposta += tassazione
        reddito += list_limiti[i]
        break
print("L'imposta del tuo reddito è di", imposta, "euro")
tassaz_media = imposta/reddito*100
print("La tassazione media è", tassaz_media, "%")