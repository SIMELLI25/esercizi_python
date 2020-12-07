input("ES 2")

listpar = []
listlen = []
listint = []
while True:
    print("quando vuoi terminare digita STOP")
    parola = input("Inserisci la prima parola: ")
    if parola == "STOP" or parola == "stop":
        break
    else:
        listpar.append(parola)
print(listpar)
for x in listpar:
    listint.append(len(x))
print("le tue parole sono formate da questo numero di lettere:")
print(listint)
for y in listpar:
    print(y, "ha",len(y), "lettere")
print("in totale ci sono", sum(listint), "lettere")