input("ES 3")

input("Rovarspraket")
parola = input("Inserisci in minuscolo la parola che vuoi tradurre in rovarspraket: ")
count1 = 0
count2 = -1
listpar = []
while True:
    if count1 == len(parola):
        break
    else:
        lett = parola[count2+1]
        listpar.append(lett)
        if lett == "a" or lett == "e" or lett == "i" or lett == "o" or lett == "u":
            print()
        else:
            listpar.append("o")
            listpar.append(lett)        
        count1 += 1
        count2 += 1
stringa = ""
for x in listpar:
    stringa += str(x)
print(stringa)