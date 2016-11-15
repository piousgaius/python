from york_graphics import *
openWindow()
def bez():
	clearCanvas()
	xCoords = []
	yCoords = []
	xlist = []
	ylist = []
	count = 1
	points = int(input("How many points do you want for the approximation? "))
	while len(xCoords) < 3:
	    x, y = waitForMouseClick()
	    xCoords.append(x)
	    yCoords.append(y)
	xIncr = (xCoords[1] - xCoords[0])/points
	yIncr = (yCoords[1] - yCoords[0])/points
	xIncr1 = (xCoords[2] - xCoords[1])/points
	yIncr1 = (yCoords[2] - yCoords[1])/points
	bezCurve = []
	while len(bezCurve) < points:
	    f = float(count)/float(points)
	    x1 = xCoords[0] + xIncr*count
	    y1 = yCoords[0] + yIncr*count
	    x2 = xCoords[1] + xIncr1*count
	    y2 = yCoords[1] + yIncr1*count
	    ly = f*(y2 - y1)
	    lx = f*(x2 - x1)
	    xlist.append(lx + xIncr*count)
	    ylist.append(ly + yIncr*count)
	    z = x1 + lx, y1 + ly
	    bezCurve.append(z)
	    count = count + 1
	print(bezCurve)
	moveTo(xCoords[0], yCoords[0])
	for i in range(points):
	    drawLine(xlist[i], ylist[i])
	updateCanvas()
