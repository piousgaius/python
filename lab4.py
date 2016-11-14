from york_graphics import *
openWindow()
coords = []
points = int(input("How many points do you want?"))
while len(coords) < points:
    x, y = waitForMouseClick()
    z = x, y
    coords.append(z)
drawPolygon(coords)
