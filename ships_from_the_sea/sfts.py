from gamegrid import *
import random

x = 900
y = 800

feld = GameGrid(x,y)
feld.setBgColor(0,105,204)
feld.setTitle("ship on the sea")
feld.show()
#ship = Actor("ship.png")
ship = Actor("./ship.png")

loc = random.randint (1,5)
if loc == 1:
    feld.addActor(ship, Location(30,95))
elif loc == 2:
    feld.addActor(ship, Location(82,618))
elif loc == 3:
    feld.addActor(ship, Location(672,300))
elif loc == 4:
    feld.addActor(ship, Location(453,567))
else:
    feld.addActor(ship, Location(823,734))
