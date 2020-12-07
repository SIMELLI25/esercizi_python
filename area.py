input("ES 4")

listfig = ["Quadrato", "Triangolo", "Rettangolo", "Cerchio"]
print(listfig)
figura = input("Inserisci di quale figura vuoi calcolare l'area tra quelle proposte di sopra: ")
if figura == "Quadrato":
    latoq = int(input("Inserisci la misura del lato del quadrato: "))
    areaq = latoq*latoq
    print("L'area del quadrato è", areaq)
elif figura == "Triangolo":
    altezzat = int(input("Inserisci la misura dell'altezza del triangolo: "))
    baset = int(input("Inserisci la misura della base del triangolo: "))
    areat = baset*altezzat//2
    print("L'area del triangolo arrotondata è", areat)
elif figura == "Rettangolo":
    baser = int(input("Inserisci la misura della base del rettagolo: "))
    altezzar = int(input("Inserisci la misura dell'altezza del rettangolo: "))
    arear = baser*altezzar
    print("L'area del rettangolo è", arear)
elif figura == "Cerchio":
    raggioc = int(input("Inserisci la misura del raggio del cerchio: "))
    areac = 3.14*pow(raggioc, 2)
    print("L'area del cerchio è", areac)