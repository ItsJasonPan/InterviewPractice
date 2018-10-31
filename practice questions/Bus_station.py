lst = [1,2,1,1,1,2,1,3]
lstL = 8

import copy
possible = {lst[0]}
for i in range(1, lstL):
    for k in range(0, i):
        possible.add(sum(lst[k:i+1]))
tmp = copy.copy(possible)
result = []
for values in possible:
    currentCount = 0
    for elements in lst:
        currentCount += elements
        if currentCount > values:
            tmp.remove(values)
            break
        elif currentCount == values:
            currentCount = 0
    if currentCount == 0:
        result.append(values)

print(result)