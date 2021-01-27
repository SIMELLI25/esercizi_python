input("ES 35")
#Organizza  con un dizionario i dati sui conti bancari con numero del conto e saldo. 
#Fornito poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.
dict_cont = {"1000":10000, "2000":25000, "3000":60000, "4000":50000, "5000":20000, "6000":75000, "7000":30000, "8000":70000}
n_conto = input("Inserisci il conto: ")
if n_conto in dict_cont:
    n_saldo = dict_cont[n_conto]
    print("Il saldo del conto", n_conto, "è di", n_saldo, "euro")
else:
    print("Il conto", n_conto, "non è presente nella mappa")