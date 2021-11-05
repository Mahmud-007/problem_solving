# Mahmudur Rahman
# 2017331093

from graphics import *

# global declarations
width = 1200
height = 900
points=[]
       
for i in range(width):
	points.append([])
	for j in range(height):
		points[i].append("blue")

def DrawAxis(win):
    
    for i in range(height):
        pt = Point(width/2,i)
        pt.draw(win)
    for i in range(width):
        pt = Point(i,height/2)
        pt.draw(win)

def ConvertPixel(x,y):
    x+=width/2
    y = -y
    y+=height/2
    return x,y

# Bressenham
def Bressenham(win,x1,y1,x2,y2):
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1==x2 and y1==y2 :
        PutPixle(win,x,y)
        
    elif y1==y2:
        if x1<x2:
           while x != x2 :
            PutPixle(win,x,y)
            x+=1
        else:
           while x != x2 :
            PutPixle(win,x,y)
            x-=1
               
    elif (x1==x2):
        if y1<y2:
            while y!=y2:
                PutPixle(win,x,y)
                y+=1
        else:
            while y!=y2:
                PutPixle(win,x,y)
                y-=1
    elif dy<dx:
        xi = 0
        yi = 0
        if x1<x2:
            xi = 1
        else:
            xi = -1
        if y1<y2:
            yi = 1
        else:
            yi = -1
        
        p = 2*dy-dx
        while x != x2:
            if p>0:
                p=p+2*(dy-dx)
                y+=yi
            else:
                p = p+2*dy
            x+=xi
            PutPixle(win,x,y)
            
    else:
        xi = 0
        yi = 0
        if x1<x2:
            xi = 1
        else:
            xi = -1
        if y1<y2:
            yi = 1
        else:
            yi = -1
        
        p = 2*dx-dy
        while y != y2:
            if p>0:
                p=p+2*(dx-dy)
                x+=xi
            else:
                p = p+2*dx
            y+=yi
            PutPixle(win,x,y)
            
    PutPixle(win,x2,y2)
    
def PutPixle(win, x, y):
    newx, newy = ConvertPixel(x,y)
    points[int(newx)][int(newy)]="bc"
    print(newx,newy)
    pt = Point(newx,newy)
    pt.draw(win)

def SwapPoint(x1,y1,x2,y2):
    t1,t2 = x1,y1 
    x1,y1 = x2,y2
    x2,y2 = t1,t2
    return x1,y1,x2,y2
	

def FloodFill(win):
	print("Click anywhere inside the polgon to fill it")
	seed_point=(win.getMouse())
	lis=[]
	lis.append(seed_point)
	fc="fc"
	oc="blue"
	while(len(lis)!=0):
            pt=lis[len(lis)-1]
            lis.pop()
            x = int(pt.getX())
            y = int(pt.getY())
            if(points[x][y]!=fc and points[x][y]==oc):
                win.plot(x,y,"red")
                points[x][y]=fc
                pt=Point(x+1,y)
                if(points[x+1][y]==oc and points[x+1][y]!=fc):
                    lis.append(pt)
                pt=Point(x,y+1)
                if(points[x][y+1]==oc and points[x][y+1]!=fc):
                    lis.append(pt)
                pt=Point(x-1,y)
                if(points[x-1][y]==oc and points[x-1][y]!=fc):
                    lis.append(pt)
                pt=Point(x,y-1)
                if(points[x][y-1]==oc and points[x][y-1]!=fc):
                    lis.append(pt)

def BoundaryFill(win):
    print("Click anywhere inside the polgon to fill it::\n")
    seed_point=win.getMouse()
    lis=[]
    lis.append(seed_point)
    fc="fc"
    bc="bc"
    while(len(lis)!=0):
        point=lis[len(lis)-1]
        lis.pop()
        x= int(point.getX())
        y= int(point.getY())
        if(points[x][y]!=fc and points[x][y]!=bc):
            win.plot(x,y,"red")
            points[x][y]=fc
            point=Point(x+1,y)
            if(points[x+1][y]!=bc and points[x+1][y]!=fc):
                lis.append(pt)
            pt=Point(x,y+1)
            if(points[x][y+1]!=bc and points[x][y+1]!=fc):
                lis.append(pt)
            pt=Point(x-1,y)
            if(points[x-1][y]!=bc and points[x-1][y]!=fc):
                lis.append(pt)
            pt=Point(x,y-1)
            if(points[x][y-1]!=bc and points[x][y-1]!=fc):
                lis.append(pt)

def main():
    print("Enter no. of sides in polygon:")
    s=int(input("Enter sides:"))
    print("Enter the points:")
    po=[]
    for i in range(s):
            print("enter x coordinate of point-",i+1,":")
            x=int(input())
            print("enter y coordinate of point-",i+1,":")
            y=int(input())
            a=[x,y]
            po.append(a)
        
    option = int(input("Enter 1 for Floodfill or anything else for Boundaryfill \n"))

    win=GraphWin("Polygon Filling ",width,height)

    DrawAxis(win)
    for i in range(s):
            x1 = po[i][0]
            y1 = po[i][1]
            x2 = po[(i+1)%s][0]
            y2 = po[(i+1)%s][1]
            Bressenham(win,x1,y1,x2,y2)

    if (option==1):
        FloodFill(win)
        win.getMouse()
        win.close()
    else:
        BoundaryFill(win)
        win.getMouse()
        win.close()

    
if __name__ == "__main__":
    main()