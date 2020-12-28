input("ES 32")
print()
#Implementa l'algoritmo per il calcolo della soluzione di un'equazione: a * x + b = 0
#se a = 0 e b = 0, equazione indeterminata
#se a = 0 e b ! 0, equazione impossibile
#se a ! 0 e b = 0, x = 0
#se a ! 0 e b ! 0, x = -b/a
a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))
if a == 0:
    if b == 0:
        print("se a = 0 e b = 0 l'equazione risulta indeterminata")
    else:
        print("se a = 0 e b =", b, "l'equazione risulta impossibile")
else:
    if b == 0:
        print("se a =", a, "e b = 0 l'equazione risulta x = 0")
    else:
        print("se a =", a, "e b =", b, "l'equazione risulta x =", -b/a)