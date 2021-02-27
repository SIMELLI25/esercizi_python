input("ES 26")
#Deriva dalla classe Quadrato una nuova classe Rettangolo aggiungendo un secondo lato per l'altezza 
#e riscrivine i metodi per il calcolo del perimetro e dell'area.
class Quadrato():
    def __init__(self, side):
        self.side = side
    def perimetro_q(self):
        p = self.side*4
        return p
    def area_q(self):
        a = self.side*self.side
        return a
class Rettangolo(Quadrato):
    def __init__(self, side, side_h):
        super().__init__(side)
        self.side_h = side_h
    def perimetro_r(self):
        p = (self.side+self.side_h)*2
        return p
    def area_r(self):
        a = self.side*self.side_h
        return a
def main():
    side = int(input("Inserisci la misura del lato del quadrato: "))
    q1 = Quadrato(side)
    print("Il perimetro del quadrato è", q1.perimetro_q())
    print("L'area del quadrato è", q1.area_q())
    side_h = int(input("Inserisci la misura del secondo lato del rettangolo: "))
    r1 = Rettangolo(side, side_h)
    print("Il perimetro del rettangolo è", r1.perimetro_r())
    print("L'area del rettangolo è", r1.area_r())
main()