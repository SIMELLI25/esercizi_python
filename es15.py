list_naz = ["Italia", "Germania", "Francia", "Spagna", "Inghilterra", "Stati Uniti", "Cina", "Giappone", "Brasile", "Argentina"]
list_cap = ["Roma", "Berlino", "Parigi", "Madrid", "Londra", "Washington", "Pechino", "Tokyo", "Brasilia", "Buenos Aires"]
nazione = input("Scegli una nazione: ")
if nazione in list_naz:
    indice = list_naz.index(nazione)
    capitale = list_cap[indice]
    print("La capitale della nazione", nazione, "è", capitale)
else:
    print("La nazione", nazione, "non è compresa nella lista")