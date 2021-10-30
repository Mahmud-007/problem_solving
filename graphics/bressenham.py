from graphics import *

# global declarations
width = 1500
height = 900
 
def  DrawAxis(win):
    for i in range(0, width):
        PutPixle(win,i,height/2)
    for i in range(0,height):
        PutPixle(win,width/2,i)

def ConvertPixel(x,y):
    x += width/2
    y = -y
    y += height/2
    return x,y

def PutPixle(win, x, y):
    pt = Point(x,y)
    pt.draw(win)
    # win.getMouse()
    # win.close()

def BresenhamLine(x1, y1, x2, y2): 
    return 0

def main():
    # x1 = int(input("Enter Start X: "))
    # y1 = int(input("Enter Start Y: ")) 
    # x2 = int(input("Enter End X: "))
    # y2 = int(input("Enter End Y: "))
    
    #BresenhamLine(x1, y1, x2, y2)

    win = GraphWin('Brasenham Line', width, height)
    DrawAxis(win)
    PutPixle(win,100, 100)
    PutPixle(win,100,200)

    for i in range(0,200):
        a,b = ConvertPixel(i,i)
        PutPixle(win,a,b)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()