def add_bin(a, b):
    carry = 0
    maxLen = max(len(a), len(b))
    result = [0] * (maxLen + 1)
    mya = ([0] * (maxLen-len(a)+1)) + list(a)
    myb = ([0] * (maxLen-len(b)+1)) + list(b)
    for i in range(-1, -(len(result)+1), -1):
        tmpA = int(mya.pop())
        tmpB = int(myb.pop())
        result[i] = (tmpA + tmpB + carry) % 2
        carry = (tmpA + tmpB + carry)//2
    for i in range(len(result)):
        result[i] = str(result[i])
    return str(int("".join(result)))

def add_bin2(a, b):
    carry = 0
    maxLen = max(len(a), len(b))
    result = [0] * (maxLen + 1)
    mya = ([0] * (maxLen-len(a)+1)) + list(a)
    myb = ([0] * (maxLen-len(b)+1)) + list(b)
    for i in range(-1, -(len(result)+1), -1):
        value = int(mya[i]) + int(myb[i]) + carry
        result[i] = (value) % 2
        carry = value//2
    for i in range(len(result)):
        result[i] = str(result[i])
    return str(int("".join(result)))
str1 = "101111"
str2 = "11000"

import time
for i in range(10):
    str1 = "10111101010101000010001010010100111110"
    str2 = "11000101001001010001011101010100111010101001010001111001010001010110"
    a = time.time()
    add_bin(str1, str2)
    b = time.time()
    str1 = "10111101010101000010001010010100111110"
    str2 = "11000101001001010001011101010100111010101001010001111001010001010110"
    c = time.time()
    add_bin2(str1, str2)
    d = time.time()
    print((b-a)/(d-c))

"""
add_bin2 is more time efficient than add_bin
"""

