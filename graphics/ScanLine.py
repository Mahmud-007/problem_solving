# Mahmudur Rahman
# 2017331093

from graphics import *

width = 1200
height = 900

def ScanLine(win,edges, n):
    Ymin = 300
    active_edges = []
    for i in range(len(edges)):
        if Ymin > edges[i][1]:
            Ymin = edges[i][1]

    while len(edges) != 0 or len(active_edges) != 0:
        p = -1
        cnty = 0
        for i in range(len(edges)):
            if edges[i][1] == Ymin:
                cnty += 1

        for i in range(0, cnty):
            for j in range(len(edges)):
                if edges[j][1] == Ymin:
                    break
            active_edges.append(edges[j])
            del edges[j:j+1]
        active_edges.sort()
        cnt = 0
        for i in range(len(active_edges)):
            if active_edges[i][3] == Ymin:
                cnt += 1
        for i in range(0, cnt):
            for j in range(len(active_edges)):
                if active_edges[j][3] == Ymin:
                    break
            del active_edges[j:j+1]
        check = True
        for i in range(len(active_edges)-1):
            Xmin = active_edges[i][0]
            Xmax = active_edges[i+1][0]
            if check == True:
                j = Xmin
                while j < Xmax:
                    win.plot(j, Ymin, "red")
                    j += 1
                check = False
            else:
                check = True
        Ymin += 1
        for i in range(len(active_edges)):
            active_edges[i][0] += active_edges[i][4]

def main():
    number_of_edge = int(input("Enter no of sides:"))

    print("Enter points:")
    po = []
    for i in range(0, number_of_edge):
        print("x coordinate of point-", i+1, ":")
        x = int(input())
        print("y coordinate of point-", i+1, ":")
        y = int(input())
        a = [x, y]
        po.append(a)

    win = GraphWin("Scan Line Algorithm for polygon filling.", width,height)
    win.setCoords(-300, -300, 300, 300)
    win.setBackground("White")
    X = Line(Point(-300, 0), Point(300, 0))
    X.draw(win)
    Y = Line(Point(0, -300), Point(0, 300))
    Y.draw(win)

    edges = []  # edge 
    for i in range(1, number_of_edge):
        x1 = po[i-1][0]
        y1 = po[i-1][1]
        x2 = po[i][0]
        y2 = po[i][1]
        if y2-y1 != 0:
            if y1 > y2:
                y1, y2 = y2, y1
                x1, x2 = x2, x1
            m = (x2-x1)/(y2-y1)
            edges.append([x1, y1, x2, y2, m])

    ScanLine(win,edges, number_of_edge)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
