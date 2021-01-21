list_naz = ["Italia", "Germania", "Francia", "Spagna", "Inghilterra", "Stati Uniti", "Cina", "Giappone", "Brasile", "Argentina"]
list_cap = ["Roma", "Berlino", "Parigi", "Madrid", "Londra", "Washington", "Pechino", "Tokyo", "Brasilia", "Buenos Aires"]
dict_tot = {}
count = 0
for j in range(len(list_naz)):
    dict_tot[list_naz[count]] = list_cap[count]
    count += 1
nazione = input("Scegli una nazione: ")
if nazione in dict_tot:
    capitale = dict_tot[nazione]
    print("La capitale della nazione", nazione, "è", capitale)
else:
    print("La nazione", nazione, "non è compresa nel dizionario")