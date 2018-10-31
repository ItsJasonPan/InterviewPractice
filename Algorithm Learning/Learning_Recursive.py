#Implement a function product to multiply 2 numbers recursively using + and - operatorsonly.

def pro(a,b):
    if b == 1:
        return a
    else:
        return a + pro(a, b-1)

#print(pro(4,10))

def flatten_list(a, result=None):
    """Flattens a nested list.

        #>>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []

    for x in a:
        if isinstance(x, list):
            flatten_list(x, result)
        else:
            result.append(x)

    return result

lst = [1,2,3,[4,5,6],[[["a"],["ba","c"], [[],[1]], "b",1]]]
print(flatten_list(lst))
myDic = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
myDic.update({"abc":42})
myDic.update()
#print(myDic)
#{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
# for x,y in myDic.items():
#    print(y)
    # print(myDic[x])

# Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
def flatten_dict(dic, result = None):
    if isinstance(dic, dict):
        pass


