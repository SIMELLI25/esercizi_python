input("ES 1")

parola = input("Inserisci la parola che vuoi controllare se è palindromo: ")
totlettere = len(parola)
listlett = []
listpal = []
count1 = 0
count2 = -1
while True:
    if totlettere == count1:
        break
    else:
        count1 += 1
        listlett.append(parola[count2+1])
        count2 += 1
listpal.extend(listlett)
listpal.reverse()
if listpal == listlett:
    print(parola, "è una parola palindroma")
else:
    print(parola, "non è una parola palindroma")