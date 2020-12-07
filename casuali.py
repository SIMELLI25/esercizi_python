input("ES 5")

from random import randint
listcas = []
listtre = []
count = 0
totn = int(input("Quanti numeri vuoi inserire nella lista? "))
while True:
    if count == totn:
        break
    else:
        count += 1
        n = randint(1, 31)
        listcas.append(n)
print("i", totn, "numeri casuali usciti sono i seguenti:")
print(listcas)
for x in listcas:
    if x % 3 == 0:
        listtre.append(x)
    else:
        continue
print("i numeri della lista divisibili pere 3 sono i seguenti", len(listtre), "numeri:")
print(listtre)