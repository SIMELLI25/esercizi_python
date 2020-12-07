input("ES 6")

from random import randint
listcas = []
listnprim = []
listrange = []
listprova = []
listprova.extend(listrange)
count = 0
totn = int(input("Quanti numeri vuoi inserire nella lista? "))
while True:
    if count == totn:
        break
    else:
        count += 1
        n = randint(1, 21)
        listcas.append(n)
print("i", totn, "numeri casuali usciti sono i seguenti:")
print(listcas)
for x in listcas:
    print("l'indice di", x, "è", listcas.index(x))
    count2 = 0
    while True:
        if count2 == len(range(2, x)):
            break
        else:
            for y in range(2, x):
                count2 += 1
                if x % y == 0:
                    listrange.append(x)
    if listrange == listprova:
        print("Il numero", x, "è primo")
        listnprim.append(x)
    else:
        print("il numero", x, "non è primo")
    listrange = []
if len(listnprim) >= 1:
    print("I numeri primi sono i seguenti:")
    print(listnprim)
else:
    print("in questa lista non ci sono numeri primi :-(")