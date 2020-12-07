input("ES 3")

input("Rovarspraket")
while True:
    parola = input("Inserisci in minuscolo la parola/frase che vuoi tradurre in rovarspraket: ")
    count1 = 0
    count2 = -1
    listpar = []
    while True:
        if count1 == len(parola):
            break
        else:
            lett = parola[count2+1]
            listpar.append(lett)
            if lett != "a" and lett != "e" and lett != "i" and lett != "o" and lett != "u":
                listpar.append("o")
                listpar.append(lett)              
            count1 += 1
            count2 += 1
    stringa = ""
    for x in listpar:
        stringa += str(x)
    print(stringa)
    remake = input("Vuoi provare con un'altra parola/frase? ")
    if remake == "no" or remake == "NO" or remake == "No":
        break