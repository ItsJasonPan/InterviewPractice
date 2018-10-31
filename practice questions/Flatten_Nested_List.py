def FNL(lst, result):
    if len(lst)==0: return None
    k = lst.pop()
    if type(k) == list:
        result.extend(FNL(k, result))
        return(result)
    else:
        result.append(k)
        return result


def FNL2(lst):
    print(lst)
    if len(lst) == 0:
        return []
    k = lst.pop()
    #lst.pop()
    a = (k==[])
    if FNL2(lst[-1]) == "no":
        FNL2()
    if k == []:
        return "no"
    else:
        #print("hi",k)
        return FNL2(k)
    if type(k)!= list:
        #print(k)
        return([k].extend(FNL2(lst)))

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return [S[0]] + flatten(S[1:])
#[[],[]]

lst = [1,2,3,[4,5,6],[[["a"],["ba","c"], [[],[1]], "b",1]]]
#print(lst[:1])
print([1,2,3]+[2,3,4])
#print(flatten(lst))

