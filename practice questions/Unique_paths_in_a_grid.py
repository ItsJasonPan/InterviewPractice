"""
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.
"""
def factorial(k):
    if k == 0:
        return 1
    elif k == 1:
        return 1
    else:
        return k*factorial(k-1)

def UPG(L):
    m = len(L)-1
    n = len(L[0])-1
    total = factorial(m+n)/(factorial(m)*factorial(n))
    #print(total)
    for row in range(len(L)):
        for col in range(len(L[0])):
            if L[row][col]==1:
                fsR, fsC = row, col
                fs = factorial(fsR+fsC)/(factorial(fsC)*factorial(fsR))
                secR, secC = m - row , n - col
                sec = factorial(secC+secR)/(factorial(secC)*factorial(secR))
                subTotal = fs * sec
                #print(fs,sec)
                total -= subTotal
                print(subTotal)
    return total

"""
BUG!!!!!!!!: double counting when have multiple obstacles
"""
L = [
    [0,0,1],
    [0,1,0],
    [0,0,0],
    [1,0,0],
    [0,0,0],
    [0,0,0],

]
#print(UPG(L))


def uniquePathsWithObstacles(A):
    paths = [[0] * len(A[0]) for i in A]
    if A[0][0] == 0:
        paths[0][0] = 1
    for i in range(1, len(A)):
        if A[i][0] == 0:
            paths[i][0] = paths[i - 1][0]
    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            paths[0][j] = paths[0][j - 1]
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    return paths[-1][-1]

# Driver Code
A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(L))

def UPG2(L):
    if L[0][0] == 1: return 0
    myL = [[0]*len(L[0]) for row in range(len(L))]
    for row in range(len(myL)):
        for col in range(len(myL[0])):
            if row == 0 and col == 0:
                myL[0][0] = 1
            elif L[row][col] == 1:
                myL[row][col] = 0
            else:
                if col == 0:
                    myL[row][col] = myL[row-1][col]
                elif row == 0:
                    myL[row][col] = myL[row][col-1]
                else:
                    myL[row][col] = myL[row][col-1] + myL[row-1][col]
    return myL[-1][-1]

print(UPG2(L))