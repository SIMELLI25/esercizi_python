input("ES 1")
#Crea una classe "Atleta" per rappresentare le informazioni su un giocatore.
#La classe deve anche contenere un attributo booleano chiamato "Visita Medica".
#Aggiungi alla classe "Atleta" un metodo per assegnare all'atleta il nome della squadra dove gioca.
#Aggiungi alla classe "Atleta" un metodo chiamato "effettua_visita" che ponga l'attributo "visitaMedica" uguale a True.
#Aggiungi alla classe "Atleta" un metodo per visualizzare i dati del giocatore
class Atleta:
    def __init__(self, name, surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height
        self.visitaMedica = False
    def informations(self):
        print("nome:", self.name)
        print("cognome:", self.surname)
        print("età:", self.age, "anni")
        print("peso:", self.weight, "chili")
        print("altezza:", self.height, "centimetri")
        if self.visitaMedica == False:
            print("L'atleta", self.surname, self.name, "non ha svolto la visita medica")
        else:
            print("L'atleta", self.surname, self.name, "ha svolto la visita medica")
    def effettua_visita(self):
        self.visitaMedica = True
        print("L'atleta", self.surname, self.name, "ha svolto la visita medica")
    def team(self, name_team):
        self.name_team = name_team
        print("L'atleta", self.surname, self.name, "gioca nella squadra", self.name_team)
atleta1 = Atleta("Simone", "Melli", 15, 65, 170)
atleta1.informations()
atleta1.team("GS Fogliano")
atleta1.effettua_visita()