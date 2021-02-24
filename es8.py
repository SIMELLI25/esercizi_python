input("ES 8")
#Crea una classe "Quadrato" con l'attributo "lato" e i metodi per il calcolo del perimetro e dell'area
class Quadrato():
    def __init__(self, lato):
        self.lato = lato
    def perimetro(self):
        perimetro = self.lato*4
        print("Il perimetro del quadrato è", perimetro, "cm")
    def area(self):
        area = self.lato*self.lato
        print("L'area del quadrato è", area, "cm^2")
def main():
    lato = int(input("Inserisci la misura del lato del quadrato: "))
    q1 = Quadrato(lato)
    q1.perimetro()
    q1.area()
main()