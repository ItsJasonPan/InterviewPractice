"""
Find the longest increasing subsequence of a given sequence / array.

In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.
"""

def LIS(L):
    myL = [0, L[0]]
    for i in L[1:]:
        if i > myL[-1]:
            myL.append(i)
        else:
            if myL[-2]<i:
                myL.pop()
                myL.append(i)
    myL.pop(0)
    return myL

L = [18, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 29, 3, 27, 7, 15]
print(LIS(L))