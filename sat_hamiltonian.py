import tkinter as tk
from tkinter import *
import math

numOfVertices = 20
while numOfVertices < 1:
    inputOfVertices = ""
    while inputOfVertices.isnumeric()!=True:
        inputOfVertices=input("Please select the number of vertices (As a single number): ")
    numOfVertices = int(inputOfVertices)


root = Tk()
root.geometry('800x800')

canvasWidth = 800
canvasHeight = 800

c=tk.Canvas(width=canvasWidth, height=canvasHeight, background="papaya whip")
c.place(x = 0, y = 0)

circleRadius = canvasHeight/8*3
circleCenter = canvasWidth/2, (canvasHeight-100)/2
vertexRadius = 20

degreesPerVertex = 360 / numOfVertices 

for i in range(numOfVertices):
    c.create_oval(circleCenter[0]+circleRadius*math.cos(math.radians(i*degreesPerVertex))-vertexRadius, circleCenter[1]+circleRadius*math.sin(math.radians(i*degreesPerVertex))-vertexRadius, circleCenter[0]+circleRadius*math.cos(math.radians(0+i*degreesPerVertex))+vertexRadius, circleCenter[1]+circleRadius*math.sin(math.radians(0+i*degreesPerVertex))+vertexRadius, fill = "white", outline = "black", width = 3, tags = ("Circle_"+str(i+1)))
for i in range(numOfVertices):
    c.create_text(circleCenter[0]+circleRadius*math.cos(math.radians(i*degreesPerVertex)), circleCenter[1]+circleRadius*math.sin(math.radians(i*degreesPerVertex)), fill = "black", text = i+1, font = ("Consolas", 15, "bold"), tags = ("Circle_"+str(i+1)))

def onClick(event):
    myTag = ""
    for i in (c.gettags("current")):
        if i.__contains__("Circle"):
            myTag = i
    if myTag != "":
        setTargeted(myTag)

selected = ""
edges = []

def setTargeted(myTag):
    global selected, edges
    myNumTag = min(c.find_withtag(myTag))
    if selected == myNumTag:
        selected = ""
        c.itemconfig(myNumTag, fill = "white")
    elif selected == "":
        selected = myNumTag
        c.itemconfig(myNumTag, fill = "red")
    else:
        if (selected, myNumTag) not in edges:
            edges.append((selected, myNumTag))
            print(edges)
            drawEdge(selected, myNumTag)
        c.itemconfig(selected, fill = "white")
        selected = ""

def drawEdge(pointId1, pointId2, color = "grey"):
    global vertexRadius
    arrowHeight = 10
    arrowWidth = 20

    x1 = (c.coords(pointId1)[0]+c.coords(pointId1)[2])/2
    y1 = (c.coords(pointId1)[1]+c.coords(pointId1)[3])/2
    x2 = (c.coords(pointId2)[0]+c.coords(pointId2)[2])/2
    y2 = (c.coords(pointId2)[1]+c.coords(pointId2)[3])/2

    percentX = ((x2-x1)**2)/((x2-x1)**2+(y2-y1)**2) 
    percentY = ((y2-y1)**2)/((x2-x1)**2+(y2-y1)**2)
    sgnY = 0
    sgnX = 0
    if (x2-x1) >= 0:
        sgnX = 1
    else: 
        sgnX = -1
    if (y2-y1) >= 0:
        sgnY = 1
    else: 
        sgnY = -1

    arrowX1 = x1 + sgnX * (percentX * (vertexRadius)**2)**(1/2)
    arrowY1 = y1 + sgnY * (percentY * (vertexRadius)**2)**(1/2)
    arrowX2 = x2 - sgnX * (percentX * (vertexRadius)**2)**(1/2)
    arrowY2 = y2 - sgnY * (percentY * (vertexRadius)**2)**(1/2)
    downTheLinePointX = arrowX2 - sgnX * (percentX * arrowHeight**2)**(1/2)
    downTheLinePointY = arrowY2 - sgnY * (percentY * arrowHeight**2)**(1/2)
    c.create_line(arrowX1, arrowY1, arrowX2, arrowY2, fill = color, width = 4, tags = "Edge_"+str(len(edges)))
    c.create_polygon(arrowX2, arrowY2, downTheLinePointX - sgnX * (arrowWidth**2 * percentY)**(1/2), downTheLinePointY + sgnY * (arrowWidth**2 * percentX)**(1/2), downTheLinePointX + sgnX * (arrowWidth**2 * percentY)**(1/2), downTheLinePointY - sgnY * (arrowWidth**2 * percentX)**(1/2), outline = color, width = 3, fill = "grey", tags = "Edge_"+str(len(edges)))


def solve():
    createCNF()
    pass

def createCNF():
    global edges, numOfVertices
    with open("formula.cnf", "w") as file:
        everyVertexVisited(numOfVertices, file)
        everyVertexMaxOnce(numOfVertices, file)


def everyVertexVisited(num, where):
    for i in range(num):
        for j in range(num):
            where.write("v"+str(i+1)+"_"+str(j+1)+" ")
        where.write("0\n")

def everyVertexMaxOnce(num, where):
    for i in range(num):
        for j in range(num):
            for k in range(num):
                if (j!=k):
                    where.write("-v"+str(i+1)+"_"+str(k+1)+" ")
                else:
                    where.write("v"+str(i+1)+"_"+str(k+1)+" ")
            where.write("0\n")




c.bind_all('<Button-1>', onClick)
button = Button(root, text='Solve', width=8, height=2, bd='10', command=solve)
button.place(x = 700, y = 720)

c.mainloop()