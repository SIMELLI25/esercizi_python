from os import system
from random import randint

input("THE MAZE")
print()
print("Benvenuto nel labirinto!")
print("Raggiungi l'uscita prima che il minotauro ti prenda")
print("il simbolo 'x' indica la tua posizione e il simbolo '#' indica la posizione del minotauro")
print("raggiungi l'uscita '+'")
print("la casella '- -' indica che puoi andare a destra o a sinistra")
print("la casella '| |' indica che puoi andare su o giù")
print("il labirinto cambia ogni volta")
input()

system("cls")

list_walls = ["- -", "| |"]

def select_wall():
  q = randint(0, 1)
  muro = list_walls[q]
  return muro

class Entity():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def move_up(self):
        self.y -= 1
    def move_down(self):
        self.y += 1
    def move_right(self):
        self.x += 1
    def move_left(self):
        self.x -= 1

class Field():
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []
    self.wall = None

  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        self.wall = select_wall()
        if x == (self.w)-1 and y == (self.h)-1:
          self.wall = self.wall.replace(" ", "+")
          self.wall_safe = self.wall
        for e in self.entities:
          if e.x == x and e.y == y:
            if e.name == "Minotauro":
              self.wall = self.wall.replace(" ", "#")
              self.wall_mino = self.wall
            elif e.name == nickname:
              self.wall = self.wall.replace(" ", "x")
              self.wall_user = self.wall
        print(self.wall, end = "")
      print()

width = 5
height = 5
nickname = input("Inserire nome: ")
s = Entity(nickname, 0, 0)
m = Entity("Minotauro", 0, height-1)
field = Field(width, height)
field.entities.append(s)
field.entities.append(m)

count = 0

while True:
  count += 1
  system("cls")
  field.draw()
  if field.wall_user == list_walls[0].replace(" ", "x"):
    print("1. sinistra")
    print("2. destra")
    move = int(input("Digita: "))
    if move == 1 and s.x > 0 and s.x <= width-1:
      s.move_left()
    elif move == 2 and s.x >= 0 and s.x < width-1:
      s.move_right()

  elif field.wall_user == list_walls[1].replace(" ", "x"):
    print("1. su")
    print("2. giù")
    move = int(input("Digita: "))
    if move == 2 and s.y >= 0 and s.y < height-1:
      s.move_down()
    elif move == 1 and s.y > 0 and s.y <= height-1:
      s.move_up()

  q = randint(0, 1)
  if field.wall_mino == list_walls[0].replace(" ", "#"):
    if q == 0 and m.x > 0 and m.x <= width-1:
      m.move_left()
    elif q == 1 and m.x >= 0 and m.x < width-1:
      m.move_right()
  elif field.wall_mino == list_walls[1].replace(" ", "#"):
    if q == 0 and m.y >= 0 and m.y < height-1:
      m.move_down()
    elif q == 1 and m.y > 0 and m.y <= height-1:
      m.move_up()

  print()
  if m.x == width-1 and m.y == height-1:
    m.x = 0
    m.y = height-1
  if s.x == width-1 and s.y == height-1:
    print("Complimenti", nickname, "hai completato il labirinto evitando il minotauro!")
    print("Hai completato il labirinto in", count, "mosse")
    break
  elif s.x == m.x and s.y == m.y:
    print("Hai perso! Sei stato raggiunto dal minotauro")
    break