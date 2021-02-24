input("ES 5-6")
#Elenca proprietà e metodi della classe prodotto
#Definisci il metodo "assegna_prezzo" della classe prodotto
class Prodotto():
    def __init__(self, name):
        self.name = name
    def assegna_prezzo(self, price):
        self.price = price
        print("Il prodotto", self.name, "costa", self.price, "€")
def main():
    name_prod = input("Inserisci il nome del prodotto: ")
    price_prod = int(input("Inserisci il prezzo del prodotto: "))
    p1 = Prodotto(name_prod)
    p1.assegna_prezzo(price_prod)
main()