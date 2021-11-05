# Mahmudur Rahman
# 2017331093

from graphics import *

# global declarations
width = 1500
height = 900

def eightWaySymmetricPlot(xc,yc,x,y,win):
   
    PutPixle(win,x+xc,y+yc)  
    PutPixle(win,x+xc,-y+yc)  
    PutPixle(win,-x+xc,-y+yc)  
    PutPixle(win,-x+xc,y+yc)  
    PutPixle(win,y+xc,x+yc)  
    PutPixle(win,y+xc,-x+yc)  
    PutPixle(win,-y+xc,-x+yc)  
    PutPixle(win,-y+xc,x+yc)  

def DrawAxis(win):    
    for i in range(height):
        pt = Point(width/2,i)
        pt.draw(win)
    for i in range(width):
        pt = Point(i,height/2)
        pt.draw(win)

def ConvertPixel(x,y):
    x += width/2
    y = -y
    y += height/2
    return x,y

def bressenhamCircle(win,xc,yc,r):
    x = 0
    y=r
    d = 3-(2*r)
    
    DrawAxis(win)
    PutPixle(win,xc,yc)
    eightWaySymmetricPlot(xc,yc,x,y,win)
    while x<=y:
        if d<0:
            d = d+(4*x)+6
        else:
            d = d+(4*x)-(4*y)+10
            y-=1
        x+=1
        eightWaySymmetricPlot(xc,yc,x,y,win)
    

def midPointCircle(win,xc,yc,r):
    x = 0
    y=r
    d = 5/float(4)-r

    DrawAxis(win)
    PutPixle(win,xc,yc)
    eightWaySymmetricPlot(xc,yc,x,y,win)
    while x<=y:
        if d<0:
            d =d+2*x+1 
        else:
            d = d+2*(x-y)+1
            y-=1
        x+=1
        eightWaySymmetricPlot(xc,yc,x,y,win)
    

def PutPixle(win, x, y):
    newx, newy = ConvertPixel(x,y)
    print("Converted x and y",newx , newy)
    pt = Point(newx,newy)
    pt.draw(win)


def PutPixle(win, x, y):
    newx, newy = ConvertPixel(x,y)
    print("Converted x and y",newx , newy)
    pt = Point(newx,newy)
    pt.draw(win)

def main():
    xc = int(input("Enter center X: "))
    yc = int(input("Enter center Y: "))
    r = int(input("Enter Radious r: "))
    option = int(input("Enter 1 for Bressenham Circle Algorithm or anything else for Midpoint circle drawing\n"))

    win = GraphWin('Circle drawing ', width, height)

    if option==1:
        bressenhamCircle(win,xc,yc,r)
        win.getMouse()
        win.close()
    else:
        midPointCircle(win,xc,yc,r)
        win.getMouse()
        win.close()

if __name__ == "__main__":
    main()