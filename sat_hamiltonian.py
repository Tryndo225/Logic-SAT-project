import subprocess
import tkinter as tk
from tkinter import *
import math


def inputParser():
    global numOfVertices
    numOfVertices = 0
    while numOfVertices < 1:
        inputOfVertices = ""
        while inputOfVertices.isnumeric() != True:
            inputOfVertices = input("Please select the number of vertices (As a single number): ")
        numOfVertices = int(inputOfVertices)
    return numOfVertices


def canvas():
    global r, c, vertexRadius, circleCenter, circleRadius, degreesPerVertex, solveButton, resultButton, resetButton, inputButton, root, inputField, parseButton
    root = Tk()
    root.geometry('800x800')
    root.title("Hamiltonian Path Solver")

    canvasWidth = 800
    canvasHeight = 800
    circleRadius = canvasHeight / 8 * 3
    circleCenter = canvasWidth / 2, (canvasHeight - 100) / 2
    vertexRadius = 20
    degreesPerVertex = 360 / numOfVertices 

    r = createCanvas(canvasWidth, canvasHeight, "Results Page:", "#9a5341")
    r.place(x=0, y=0)

    c = createCanvas(canvasWidth, canvasHeight, "Input Page:", "papaya whip")
    c.place(x=0, y=0)
    c.bind_all('<Button-1>', onClick)
    
    inputButton = Button(r, text='Input', width=3, height=1, bd='10', command=inputPage)
    inputButton.place(x=770, y=725, anchor="center")
    resultButton = Button(c, text='Results', width=3, height=1, bd='10', command=resultPage)
    resultButton.place(x=770, y=725, anchor="center")
    solveButton = Button(root, text='Solve', width=3, height=1, bd='10', command=solve)
    solveButton.place(x=30, y=725, anchor="center")
    resetButton = Button(root, text='Reset', width=3, height=1, bd='10', command=reset)
    resetButton.place(x=30, y=775, anchor="center")
    inputField = Text(root, height = 4, width = 80) 
    inputField.place(x=400, y=750, anchor="center")
    parseButton = Button(root, text='Parse', width=3, height=1, bd='10', command=parse)
    parseButton.place(x=770, y=775, anchor="center")
    
    root.mainloop()

def createCanvas(sizeX, sizeY, title, backgroundColor):
    canvas = tk.Canvas(width=sizeX, height=sizeY, background=backgroundColor)
    for i in range(numOfVertices):
        canvas.create_oval(circleCenter[0] + circleRadius * math.cos(math.radians(i * degreesPerVertex)) - vertexRadius, circleCenter[1] + circleRadius * math.sin(math.radians(i * degreesPerVertex)) - vertexRadius, circleCenter[0] + circleRadius * math.cos(math.radians(0 + i * degreesPerVertex)) + vertexRadius, circleCenter[1] + circleRadius * math.sin(math.radians(0 + i * degreesPerVertex)) + vertexRadius, fill="white", outline="black", width=3, tags=("Circle_" + str(i + 1)))
    for i in range(numOfVertices):
        canvas.create_text(circleCenter[0] + circleRadius * math.cos(math.radians(i * degreesPerVertex)), circleCenter[1] + circleRadius * math.sin(math.radians(i * degreesPerVertex)), fill="black", text=i + 1, font=("Consolas", 15, "bold"), tags=("Circle_" + str(i + 1)))
    canvas.create_text(5, 5, font=("Consolas", 25, "bold"), anchor="nw", text=title, tags="Title")
    return canvas

def parse():
    global edges
    edges.clear()
    inp = inputField.get(1.0, "end-1c")
    for i in inp.split(';'):
        last = ""
        for j in i.split(','):
            j=j.replace(" ", "").replace("(", "").replace(")", "")
            if last == "":
                last = j
            else:
                edges.append((int(last), int(j)))
    drawEdges(c)

def insert():
    global edges
    inputField.delete(1.0, "end")
    text = ""
    for i in range(len(edges)):
        text+="("+str(edges[i][0])+","+str(edges[i][1])+")"
        if i != len(edges)-1:
            text += ";"
    inputField.insert(1.0, text)


def reset():
    global selected, edges
    root.destroy()
    selected = ""
    edges = []
    canvas()

def buttonsToTop():
    tk.Misc.lift(solveButton)
    tk.Misc.lift(resetButton)
    tk.Misc.lift(inputField)
    tk.Misc.lift(parseButton)


def resultPage():
    tk.Misc.lift(r)
    buttonsToTop()

    
def inputPage():
    tk.Misc.lift(c)
    buttonsToTop()

def onClick(event):
    myTag = ""
    for i in (c.gettags("current")):
        if i.__contains__("Circle"):
            myTag = i
    if myTag != "":
        setTargeted(myTag)


def setTargeted(myTag):
    global selected, edges
    myNumTag = min(c.find_withtag(myTag))
    if selected == myNumTag:
        selected = ""
        c.itemconfig(myNumTag, fill="white")
    elif selected == "":
        selected = myNumTag
        c.itemconfig(myNumTag, fill="red")
    else:
        if (selected, myNumTag) not in edges:
            edges.append((selected, myNumTag))
        else:
            deleteEdge(selected, myNumTag)
        drawEdges(c)
        insert()
        c.itemconfig(selected, fill="white")
        selected = ""


def drawEdges(canvas):
    canvas.delete("Edge")
    for i in edges:
        drawEdge(i[0], i[1], canvas)
        

def drawEdge(pointId1, pointId2, canvas, color="grey", tag=""):
    global vertexRadius
    arrowHeight = 10
    arrowWidth = 20

    x1 = (canvas.coords(pointId1)[0] + canvas.coords(pointId1)[2]) / 2
    y1 = (canvas.coords(pointId1)[1] + canvas.coords(pointId1)[3]) / 2
    x2 = (canvas.coords(pointId2)[0] + canvas.coords(pointId2)[2]) / 2
    y2 = (canvas.coords(pointId2)[1] + canvas.coords(pointId2)[3]) / 2

    percentX = ((x2 - x1) ** 2) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) 
    percentY = ((y2 - y1) ** 2) / ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    sgnY = 0
    sgnX = 0
    if (x2 - x1) >= 0:
        sgnX = 1
    else: 
        sgnX = -1
    if (y2 - y1) >= 0:
        sgnY = 1
    else: 
        sgnY = -1

    arrowX1 = x1 + sgnX * (percentX * (vertexRadius) ** 2) ** (1 / 2)
    arrowY1 = y1 + sgnY * (percentY * (vertexRadius) ** 2) ** (1 / 2)
    arrowX2 = x2 - sgnX * (percentX * (vertexRadius) ** 2) ** (1 / 2)
    arrowY2 = y2 - sgnY * (percentY * (vertexRadius) ** 2) ** (1 / 2)
    downTheLinePointX = arrowX2 - sgnX * (percentX * arrowHeight ** 2) ** (1 / 2)
    downTheLinePointY = arrowY2 - sgnY * (percentY * arrowHeight ** 2) ** (1 / 2)
    if tag == "":
        tag = "Edge"
    canvas.create_line(arrowX1, arrowY1, arrowX2, arrowY2, fill=color, width=4, tags=tag)
    canvas.create_polygon(arrowX2, arrowY2, downTheLinePointX - sgnX * (arrowWidth ** 2 * percentY) ** (1 / 2), downTheLinePointY + sgnY * (arrowWidth ** 2 * percentX) ** (1 / 2), downTheLinePointX + sgnX * (arrowWidth ** 2 * percentY) ** (1 / 2), downTheLinePointY - sgnY * (arrowWidth ** 2 * percentX) ** (1 / 2), outline=color, width=3, fill=color, tags=tag)

def deleteEdge(pointId1, pointId2):
    index = ""
    for i in range(len(edges)):
        if edges[i] == (pointId1, pointId2):
            index = i
    if index!="":
        edges.pop(index)

def solve():
    r.delete("resultLine")
    resultPage()
    createCNF()
    resultPrint(subprocess.run(["glucose", "formula.cnf", "-model"], stdout=subprocess.PIPE))


def createCNF():
    global edges, numOfVertices
    clauses = []
    comments = 0
    clauses, comments = oneVertexAtPos(numOfVertices, clauses, comments)
    clauses, comments = everyVertexMaxOnce(numOfVertices, clauses, comments)
    clauses, comments = everyVertexVisited(numOfVertices, clauses, comments)
    clauses, comments = maxOneVertexAtEachPos(numOfVertices, clauses, comments)
    clauses, comments = pathConsistOfActualEdges(numOfVertices, clauses, comments)
    with open("formula.cnf", "w") as file:
        file.write("p cnf " + str(numOfVertices ** 2) + " " + str(len(clauses) - comments) + '\n')
        for i in clauses:
            if isinstance(i, str):
                file.write(i)
            else:
                for j in i:
                    file.write(str(j))
                    file.write(" ")
                file.write("0\n")


def oneVertexAtPos(num, clauses, comments):
    clauses.append("c One vertex at each position\n")
    comments += 1
    for i in range(num):
        tmp = []
        for j in range(num):
            tmp.append(numOfVertices * (j) + (i + 1))
        clauses.append(tmp)
    return clauses, comments


def everyVertexMaxOnce(num, clauses, comments):
    clauses.append("c Every vertex visited max once\n")
    comments += 1
    for i in range(num):
        for j in range(num):
            for k in range(j, num):
                if numOfVertices * (i) + (j + 1) != numOfVertices * (i) + (k + 1):
                    tmp = []
                    tmp.append(-1 * (numOfVertices * (i) + (j + 1)))
                    tmp.append(-1 * (numOfVertices * (i) + (k + 1)))
                    clauses.append(tmp)
    return clauses, comments


def everyVertexVisited(num, clauses, comments):
    clauses.append("c Every vertex visited at least once\n")
    comments += 1
    for i in range(num):
        tmp = []
        for j in range(num):
            tmp.append(numOfVertices * (i) + (j + 1))
        clauses.append(tmp)
    return clauses, comments


def maxOneVertexAtEachPos(num, clauses, comments):
    clauses.append("c Max one vertex at each position\n")
    comments += 1
    for i in range(num):
        for j in range(num):
            for k in range(j, num):
                if numOfVertices * (j) + (i + 1) != numOfVertices * (k) + (i + 1):
                    tmp = []
                    tmp.append(-1 * (numOfVertices * (j) + (i + 1)))
                    tmp.append(-1 * (numOfVertices * (k) + (i + 1)))
                    clauses.append(tmp)
    return clauses, comments


def pathConsistOfActualEdges(num, clauses, comments):
    clauses.append("c Path consist only of valid edges\n")
    comments += 1
    for i in range(num):
        for j in range(num):
            if (i + 1, j + 1) not in edges and i != j:
                for k in range(num - 1):
                        pos1 = k + 1
                        pos2 = k + 2
                        tmp = []
                        tmp.append(-1 * (numOfVertices * (i) + (pos1)))
                        tmp.append(-1 * (numOfVertices * (j) + (pos2)))
                        clauses.append(tmp)
    return clauses, comments


def resultPrint(result):
    for line in result.stdout.decode('utf-8').split('\n'):
        print(line)

    if (result.returncode == 20):
        return
    
    vars = []
    for line in result.stdout.decode('utf-8').split('\n'):
        if line.startswith("v"):
            vars = line.split(" ")
            vars.remove("v")
            vars.remove("0")
    
    decodedPath = decodeResult(vars)
    drawResult(decodedPath)

    print()
    print("##################################################################")
    print("###########[ Human readable result of the tile puzzle ]###########")
    print("##################################################################")
    print()
    print("Hamiltonian path goes as through vertexes as follows:", end=" ")
    for i in decodedPath.keys():
        print(i, end=" ")
    print()


def decodeResult(vars):
    path = []
    for i in vars:
        if (int(i) > 0):
            path.append(int(i))
    print(path)
    
    decodedPath = {}
    for i in range(len(path)):
        decodedPath[str(i + 1)] = path[i] - (numOfVertices * i)
    print(decodedPath)
    
    decodedPath = dict(sorted(decodedPath.items(), key=lambda x:x[1]))
    return decodedPath


def drawResult(path):
    last = ""
    for i in path:
        if last == "":
            last = i
        else:
            drawEdge(last, i, r, "green", "resultLine")
            last = i


if __name__ == "__main__":
    global selected, edges, drawn
    selected = ""
    edges = []
    drawn = []
    inputParser()
    canvas()
