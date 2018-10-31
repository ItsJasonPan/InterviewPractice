def roman_To_Integer(str):
    """
    "I" = 1
    "V" = 5
    "X" = 10
    "L" = 50
    "C" = 100
    "D" = 500
    "M" =1000
    """
    def rec(myL, start, end, index, list):
        if start == end: return 0
        else:
            if start == -1: # to the left
                if list[index] in myL[:end]:
                    result = lst.count(1000) * 1000
                    # to the left
                    left = rec(myL, -1, end, index, list)
                    right = rec(myL, start, end, index, list)
                    return result + 42
            return
    lst = list(str)
    for i in range(len(lst)):
        if lst[i] == "I": lst[i] = 1
        elif lst[i] == "V": lst[i] = 5
        elif lst[i] == "X": lst[i] = 10
        elif lst[i] == "L": lst[i] = 50
        elif lst[i] == "C": lst[i] = 100
        elif lst[i] == "D": lst[i] = 500
        elif lst[i] == "M": lst[i] = 1000
        else:
            print("Invalid Roman Numeral")
            return None
    result = 0
    if 1000 in lst:
        result += lst.count(1000) * 1000

def RTI(S):
    result = 0
    for i in range(len(S)):
        char = S[len(S) - i - 1]
        if char == "I":
            result += (-1 if result >= 5 else 1)
        elif char == "V":
            result += 5 * (-1 if result >= 10 else 1)
        elif char == "X":
            result += 10 * (-1 if result >= 50 else 1)
        elif char == "L":
            result += 50 * (-1 if result >= 100 else 1)
        elif char == "C":
            result += 100 * (-1 if result >= 500 else 1)
        elif char == "D":
            result += 500 * (-1 if result >= 1000 else 1)
        elif char == "M":
            result += 1000
    return result

print(RTI("MMI"))
