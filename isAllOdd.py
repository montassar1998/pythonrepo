from audioop import reverse
from functools import reduce


def isAllEven(lst):
    sum = list(map(lambda x: (x % 2 == 0), lst))
    print(sum)
    sum = reduce(lambda a, b: (b and a), sum, True)
    print(sum)
    return sum


print(isAllEven([4, 4, 3]))

# my method for reversing a dictionary
testDict = {"a": "1", "b": "2", "c": "3", "d": '4'}


def swapKeys(dct):
    resDict = dict(zip(testDict.values(), testDict.keys()))
    return resDict


print(swapKeys(testDict))


# method 2
def swapKeysV2(dict):
    res = {j: i for i, j in dict.items()}
    return res


print(swapKeysV2(testDict))
a = "abxay"
b = "abeaf"


def HammingDist(a, b):
    Hd = 0
    for i, j in (zip(a, b)):
        Hd += (i != j)
    return Hd


print(HammingDist(a, b))
