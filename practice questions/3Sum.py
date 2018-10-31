"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
如何做到 O(n^2) 的时间复杂度？
"""
def threeSum(L):
    myL = []
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            for k in range(j+1, len(L)):
                if L[i]+L[j]+L[k] == 0:
                    if sorted([L[i], L[j], L[k]]) not in myL:
                        myL.append(sorted([L[i], L[j], L[k]]))
    return myL

import time
S = [-1, 0, 1, 2, -1, -4,0,1,5,0]
print(threeSum(S))
