"""
https://www.interviewbit.com/problems/ways-to-decode/

A message containing letters from A-Z is being encoded to numbers using the following mapping
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


def numDecodings(A):
    mylst = [0]*len(A)
    if int(A[0]) == 0:
        return 0
    mylst[0] = 1
    try:
        for i in range(1, len(A)):
            if int(A[i]) == 0:
                if int(A[i-1]) == 1 or int(A[i-1]) == 2:
                    mylst[i - 1] = mylst[i - 2]
                    mylst[i] = mylst[i-1]
                else: return 0
            elif int(A[i-1]) == 0:
                mylst[i] = mylst[i-1]
            elif 10 <= int(A[i-1:i+1]) <= 26:
                if i == 1:
                    mylst[i] = mylst[i-1] + 1
                else:
                    mylst[i] = mylst[i-1] + mylst[i-2]
            else:
                mylst[i] = mylst[i-1]
            #print(mylst)
        return mylst[-1]
    except Exception:
        return 0


# official solution
def numDecodings2(A):
    if A=='0' or A[0]=='0':
        return 0
    n=len(A)
    a=[0]*n
    a[0]=1
    for i in range(1, n):
        if A[i]=='0' and not (A[i-1] == '1' or A[i-1] =='2'):
            return 0
        elif A[i]=='0':
            if i==1:
                a[i]= 1
            else:
                a[i]= a[i-2]
        elif A[i-1]=='0':
            a[i]= a[i-1]
        elif int( A[ i-1:i+1]) <=26:
            if i==1:
                a[i]= 2
            else:
                a[i]= a[i-1] + a[ i-2]
        else:
            a[i]= a[i-1]
    return a[ n-1]
#print(numDecodings("1212"))
def check(str):
    print(numDecodings(str))
    print(numDecodings2(str))

check("12102023141123132011231232022023134123204")
