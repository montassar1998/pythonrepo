n = int(input("Saisir un entier strictement positif "))
while(n <= 0):
    try:
        n = int(input("Saisir un entier strictement positif "))
    except ValueError:
        print("please respect the criteria")
# odd numbers method 1
for i in range(1, n+1, 2):
    print(i, end=" ")
print()
# odd numbers method 2
counter = 1
while(counter <= n):
    print(counter, end=" ")
    counter += 2
print("")
# count the number of digits
sizen = len(str(n))
print(f"the number contains {sizen} digit/s")

# activity 4
"""same size n as before"""
L = []
# read and remove duplicates
for i in range(n):
    ch = input("saisir un element ")
    L.append(ch)
print(L)
X = set(L)
print(X)

# activity 5

jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois = ["January", "February", "March", "April", "May", "June", "July", "August ",
        "September", "October", "November", "December"]
mjList = list(zip(mois, jours))
mjDict = dict(zip(mois, jours))

print(mjList)
print(mjDict)

# activity 6
""" n = int(input("input dict size"))
d1 = {}
d2 = {}
d3 = {}
for i in range(3):
    print(f"reading dict {i}")
    for j in range(n):
        key = input("Enter a dict key ")
        value = input("enter a dict value")
        if(i == 0):
            d1[key] = value
        elif (i == 1):
            d2[key] = value
        else:
            d3[key] = value """
d1 = {"a": 1, "d": 4, "g": 7}
d2 = {"a": 1, "b": 2, "h": [8, 11]}
d3 = {"a": 2, "c": 3, "h": 9}


def merge(*dicts):
    d = {}

    for dict in dicts:
        for key in dict:
            print(f"dict avant  = {d}")
            try:

                d[key].append(dict[key])
                print(f"dict[{key}] = {dict[key]} type = {type(dict[key])}")

            except KeyError:

                elements = dict[key] if type(
                    dict[key]) is list else [dict[key]]
                print(f"key error new key = {elements}")
                # splits if it found a list
                d[key] = elements
            print(f"dict apres = {d}  typeNew = {type(dict[key])}")
    return d


d1 = merge(d1, d2, d3)
print(d1, d2, d3, sep="\n")
# sort it
print(d1)
