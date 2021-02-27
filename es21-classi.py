input("ES 21")
#Data la classe "Motociclo" creata nel problema 7 deriva la classe "CICLOMOTORE".
#Aggiungi le proprietà opportune e modifica il metodo che consente di visualizzare i valori delle proprietà.
class Motociclo():
    def __init__(self, template, color, price, max_speed):
        self.template = template
        self.color = color
        self.price = price
        self.max_speed = max_speed
    def info(self):
        print("Modello:", self.template)
        print("Colore:", self.color)
        print("Prezzo:", self.price, "€")
        print("Velocità massima:", self.max_speed, "km/h")
class Ciclomotore(Motociclo):
    def __init__(self, template, color, price, max_speed, displacement):
        super().__init__(template, color, price, max_speed)
        self.displacement = displacement
    def info(self):
        super().info()
        print("Cilindrata:", self.displacement)
def main():
    modello = input("Inserisci il modello del motociclo: ")
    colore = input("Inserisci il colore del motociclo: ")
    prezzo = int(input("Inserisci il prezzo del motociclo: "))
    max_velocita = int(input("Inserisci la massima velocità del motociclo: "))
    m1 = Motociclo(modello, colore, prezzo, max_velocita)
    m1.info()
    input()
    modello = input("Inserisci il modello del ciclomotore: ")
    colore = input("Inserisci il colore del ciclomotore: ")
    prezzo = int(input("Inserisci il prezzo del ciclomotore: "))
    max_velocita = int(input("Inserisci la massima velocità del ciclomotore: "))
    cilindrata = int(input("Inserisci il valore della cilindrata del ciclomotore: "))
    c1 = Ciclomotore(modello, colore, prezzo, max_velocita, cilindrata)
    c1.info()
main()