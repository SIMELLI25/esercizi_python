input("ES 31")
#Un'azienda vende prodotti in tutta Italia e la rete di vendita è suddivisa in quattro zone: Nord, Centro, Sud e isole.
#Dopo aver acquisito in un array il fatturato nelle quattro zone, calcola il totale del fatturato
#e i valori in percentuale delle vendite nelle quattro zone rispetto al totale.
list_zone = ["Nord", "Centro", "Sud", "Isole"]
list_fatt = []
fatt_tot = 0
for i in range(4):
    print("Inserisci il fatturato della zona", list_zone[i])
    fatturato = int(input("fatturato: "))
    list_fatt.append(fatturato)
    fatt_tot += fatturato
print("Il fatturato totale è di", fatt_tot, "euro")
for i in range(4):
    percentuale = list_fatt[i]/fatt_tot*100
    round(percentuale, 2)
    print("La percentuale di vendita nella zona", list_zone[i], "è", percentuale, "%")