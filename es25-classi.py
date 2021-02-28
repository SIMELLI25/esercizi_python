input("ES 25")
#Crea la classe Triangolo, la classe derivata TriangoloIsoscele e, da quest'ultima, la classe derivata TriangoloEquilatero.
class Triangolo():
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    def info_s(self):
        print("Il triangolo è scaleno")
        print("Il perimetro del triangolo è", self.side_1+self.side_2+self.side_3)
class TriangoloIsoscele(Triangolo):
    def __init__(self, side_1, side_2, side_3):
        super().__init__(side_1, side_2, side_3)
    def info_i(self):
        print("Il triangolo è isoscele")
        print("Il perimetro del triangolo è", self.side_1+self.side_2+self.side_3)
class TriangoloEquilatero(TriangoloIsoscele):
    def __init__(self, side_1, side_2, side_3):
        super().__init__(side_1, side_2, side_3)
    def info_e(self):
        print("Il triangolo è equilatero")
        print("Il perimetro del triangolo è", self.side_1*3)
def main():
    side_1 = int(input("Inserisci la misura del primo lato: "))
    side_2 = int(input("Inserisci la misura del secondo lato: "))
    side_3 = int(input("Inserisci la misura del terzo lato: "))
    if side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
        t1 = Triangolo(side_1, side_2, side_3)
        t1.info_s()
    elif side_1 == side_2 and side_1 == side_3 and side_2 == side_3:
        t1 = TriangoloEquilatero(side_1, side_2, side_3)
        t1.info_e()
    else:
        t1 = TriangoloIsoscele(side_1, side_2, side_3)
        t1.info_i()
main()