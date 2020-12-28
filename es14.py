input("ES 14")
print()
print("Scrivi un programma che scriva la differenza di due numeri a e b se a*b > 10.")
print("Se a*b =< 10 scrivi un programma che scriva la somma.")
print("Eseguilo poi per diverse coppie di valori a e b.")
input()
print()
a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
if a*b <= 10:
    print("La somma di", a, "e", b, "è", a+b)
else:
    print("La differenza di", a, "e", b, "è", a-b)
# se a = -5 e b = 2, a*b = -10 e a+b = -3
# se a = 5 e b = -5, a*b = -25 e a+b = 0
# se a = 10 e b = 2, a*b = 20 e a-b = 8
# se a = -4 e b = -5, a*b = 20 e a-b = 1
# se a = 5 e b = 4, a*b = 20 e a-b = 1
# se a = -3 e b = -2, a*b = 6 e a+b = -5