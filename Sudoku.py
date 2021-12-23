def isValid(grid,row,col,num):
    for i in range(9):
        if (grid[row][i]==num):
            return False
        if (grid[i][col]==num):
            return False
    startRow = row - row%3
    startCol = col - col%3
    for i in range(3):
        for j in range(3):
            if (grid[i+startRow][j+startCol]==num):
                return False
    return True

def solve_sudoku(grid,x,y):
    if (x==9):
        display(grid)
        return
    new_x = 0
    new_y = 0

    if (y == 8): # for 9*9 sudoku grid
        new_y = 0
        new_x = x+1
    else: 
        new_x = x
        new_y = y+1
    if (grid[x][y]!=0):
        solve_sudoku(grid,new_x,new_y) #if cell is non zero then go for the next cell
        #print(x," ",y)
    else:
        for i in range(1,10):
            #print(i)
            if (isValid(grid,x,y,i)):
                #print(i)
                grid[x][y]=i
                #print(grid[x][y])
                #print(x," ",y)
                solve_sudoku(grid,new_x,new_y)
                grid[x][y]=0
def display(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end = " ")
        print()
N = 9
grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
       [5, 2, 0, 0, 0, 0, 0, 0, 0],
       [0, 8, 7, 0, 0, 0, 0, 3, 1],
       [0, 0, 3, 0, 1, 0, 0, 8, 0],
       [9, 0, 0, 8, 6, 3, 0, 0, 5],
       [0, 5, 0, 0, 9, 0, 6, 0, 0],
       [1, 3, 0, 0, 0, 0, 2, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 7, 4],
       [0, 0, 5, 2, 0, 6, 3, 0, 0]]

solve_sudoku(grid,0,0)
