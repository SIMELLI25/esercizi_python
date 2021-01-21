list_naz = ["Italia", "Germania", "Francia", "Spagna", "Inghilterra", "Stati Uniti", "Cina", "Giappone", "Brasile", "Argentina"]
list_cap = ["Roma", "Berlino", "Parigi", "Madrid", "Londra", "Washington", "Pechino", "Tokyo", "Brasilia", "Buenos Aires"]
dict_tot = {}
count = 0
for j in range(len(list_naz)):
    dict_tot[list_cap[count]] = list_naz[count]
    count += 1
capitale = input("Scegli una capitale: ")
if capitale in dict_tot:
    nazione = dict_tot[capitale]
    print(capitale, "è capitale della nazione", nazione)
else:
    print("La capitale", capitale, "non è compresa nel dizionario")