def painthouse(M):
    if len(M) == 0: return 0
    n = len(M)
    for i in range(1, n):
        M[i][1] += min(M[i - 1][0], M[i - 1][2])
        M[i][2] += min(M[i - 1][0], M[i - 1][1])
        M[i][0] += min(M[i - 1][1], M[i - 1][2])
    return min(M[n-1])

M =[]
#M = [[1,2,3],[1,2,3],[1,2,3],[4,5,6],[8,9,10],[1,0,3]]
print(painthouse(M))
