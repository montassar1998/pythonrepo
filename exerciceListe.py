InitialList = [[0, "a"], [2, "b"], [3, "c"]]
byTwo = []
for i in InitialList:
    res = list(map(lambda x: x*2, i))
    byTwo.append(res)
print(InitialList)
print(byTwo)


newList = [n*2 for i in InitialList for n in i]
print(newList)

lettersByThree = [n*3 if type(n) == str else n *
                  2 for i in InitialList for n in i]
print(lettersByThree)

# Instructor's code below


# Question1
n = int(input("tapez la taille des 3 dictionnaires"))
dict1 = {input("tapez la clef "+str(i+1) + " du dictionnaire 1"): input("tapez la valeur "+str(i+1)+" du dictionnaire 1") for i in
         range(n)}
dict2 = {input("tapez la clef "+str(i+1) + " du dictionnaire 2"): input("tapez la valeur "+str(i+1)+" du dictionnaire 2") for i in
         range(n)}
dict3 = {input("tapez la clef "+str(i+1) + " du dictionnaire 3"): input("tapez la valeur "+str(i+1)+" du dictionnaire 3") for i in
         range(n)}

# Question2
dict1 = {"a": 1, "d": 4, "g": 7}
dict2 = {"a": 1, "b": 2, "h": [8, 11]}
dict3 = {"a": 2, "c": 3, "h": 9}

Dfusion = {}
L = []
for i in set(list(dict1.keys())+list(dict2.keys())+list(dict3.keys())):
    for j in (dict1, dict2, dict3):
        if i in j:
            L.append(j[i])
    Dfusion[i] = L
    L = []

print(f" le dictionnaire  aprés fusion {Dfusion}")
