from graphics import *

# global declarations
width = 1500
height = 900
 
def  DrawAxis(win):
    for i in range(0, width):
        #PutPixle(win,i,height/2)
        pt = Point(i,height/2)
        pt.draw(win)
    for i in range(0,height):
        #PutPixle(win,width/2,i)
        pt = Point(width/2,i)
        pt.draw(win)

def ConvertPixel(x,y):
    x += width/2
    y = -y
    y += height/2
    return x,y

def SwapPoint(x1,y1,x2,y2):
    t1,t2 = x1,y1 
    x1,y1 = x2,y2
    x2,y2 = t1,t2
    return x1,y1,x2,y2 

def PutPixle(win, x, y):
    a,b = ConvertPixel(x,y)
    pt = Point(a,b)
    pt.draw(win)
    
# DDA
def DDA(win,x1, y1, x2, y2): 
    dy = y2-y1
    dx = x2-x1   
    m = float(dy/dx)
    if (dy==0):
        if (x2<x1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)
        for i in range(x1,x2):
            PutPixle(win,i,y1)

    elif (dx==0):
        if (y2<y1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)
        for i in range(y1,y2):
            PutPixle(win,x1,i)
             
    elif (abs(dy)>=abs(dx)):

        if (y2<y1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)

        x=x1  
        for i in range(y1,y2+1):
            a = int(x)
            PutPixle(win,a,i)
            print(a,i)
            x += (1/m)
    else:
        if (x2<x1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)

        y=y1  
        for i in range(x1,x2+1):
            a = int(y)
            PutPixle(win,i,a)
            print(i,a)
            y += m
# Bressenham
def Bressenham(win,x1,y1,x2,y2):
    dy = y2-y1
    dx = x2-x1 
    
    if (dy==0):
        if (x2<x1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)
        for i in range(x1,x2):
            PutPixle(win,i,y1)

    elif (dx==0):
        if (y2<y1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)
        for i in range(y1,y2):
            PutPixle(win,x1,i)
             
    elif (abs(float(dy/dx))>=1):
        if (y2<y1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)

        if x1<x2:
            xi = 1
        else:
            xi = -1

        if y1<y2:
            yi = 1
        else:
            yi = -1

        dk = 2*dy - dx 

        while(y1<=y2):
            if (dk<0):
                PutPixle(win,x1,y1)
                dk += 2*dx
            else:
                PutPixle(win,x1,y1)
                x1 += xi
                dk += 2*(dx-dy)
            y1+=yi  
    else:
        if (x2<x1):
            x1,y1,x2,y2 = SwapPoint(x1,y1,x2,y2)

        if x1<x2:
            xi = 1
        else:
            xi = -1

        if y1<y2:
            yi = 1
        else:
            yi = -1

        print("else",x1,y1) 
        dk = 2*dy - dx 

        while(x1<=x2):
            if (dk>0):
                PutPixle(win,x1,y1)
                dk += 2*(dy-dx)
                y1+=yi
            else: 
                PutPixle(win,x1,y1)
                dk+=2*dy
            print("else",x1,y1)
            x1+=xi
def main():   
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: ")) 
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))

    option = int(input("Press 1 for DDA and anything else for Bressenham: "))

    win = GraphWin('Line Drwaing', width, height)
    DrawAxis(win)

    if(option==1):  
        DDA(win,x1,y1,x2,y2)
        win.getMouse()
        win.close()
    
    else:
        Bressenham(win,x1,y1,x2,y2)
        win.getMouse()
        win.close()
    

if __name__ == "__main__":
    main()