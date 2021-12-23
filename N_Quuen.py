def isSafe(x,y):
    for i in range(x):
        if (board[i][y]==1):
            return False
        for i,j in zip(range(x,-1,-1),range(y,-1,-1)):
            if (board[i][j]==1):
                return False
        for i,j in zip(range(x,-1,-1),range(y,N,1)):
            if (board[i][j]==1):
                return False
    return True
  


def solve_N_Queeen(row):
    if (row>=N):
        return True
    for i in range(N):
        if (isSafe(row,i)):
            board[row][i]=1
            if (solve_N_Queeen(row+1)):
                return True
            board[row][i]=0
    return False

N = 4
board =[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],]
solve_N_Queeen(0)
for i in range(N):
    for j in range(N):
        print(board[i][j], end = " ")
    print()