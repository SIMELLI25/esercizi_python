input("ES 7")
#Elenca proprietà e metodi della classe "Monociclo"
class Monociclo():
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
def main():
    modello = input("Inserisci il modello del monociclo: ")
    colore = input("Inserisci il colore del monociclo: ")
    prezzo = int(input("Inserisci il prezzo del monociclo: "))
    max_velocita = int(input("Inserisci la massima velocità del monociclo: "))
    m1 = Monociclo(modello, colore, prezzo, max_velocita)
    m1.info()
main()