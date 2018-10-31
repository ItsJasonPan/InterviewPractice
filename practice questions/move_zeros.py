def moverZeros(L):
    if len(L) == 0: return None
    i = 0
    numOfZero = 0
    while i < len(L)-numOfZero-1:
        if L[i] == 0:
            L.append(L.pop(i))
            numOfZero += 1
        else:
            i += 1
    return L


L = [8, 7, 0, 1, 0, 0, 3, 0, 12, 0, 9, 8]
print(moverZeros(L))