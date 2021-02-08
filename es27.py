input("ES 27")
#Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. 
#Fornito poi il nome della persona, il programma visualizza il suo numero di telefono 
#oppure un messaggio nel caso la persona non sia presente nella rubrica
dict_rubrica = {
    "Simone Melli":"370 365 5766",
    "Enrico Rossi":"353 794 6890",
    "Matteo Zaccarelli":"333 853 8922",
    "Niccolò Panciroli":"340 787 8574",
    "Francesco Righetti":"396 954 2335",
    "Riccardo Malavasi":"324 962 5291",
    "Egor Shvechikov":"356 839 2496"
}
persona = input("Chi vuoi chiamare? ")
if persona in dict_rubrica:
    print("Il numero telefonico di", persona, "è", dict_rubrica[persona])
else:
    print(persona, "non è presente nella rubrica")