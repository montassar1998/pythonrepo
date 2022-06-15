from ast import In
import calendar
from datetime import date
from distutils.log import error
print("Hello")
for i in range(1, 11):
    print(str(i)+" bien bien {0}".format(i+1))
lst = []


def fact(n): return 1 if n == 0 else n*fact(n-1)


print(fact(5))
# package et module
# types élémentaires simples


# complex, int, complex numeric type
print(pow(2, 3))
# print(float(input())/2)
print("7.9".isdigit())


# Les conteneurs
# list, mutable et ordonnée   , hétérogénes
L = [1, 2, 3, 4, "ab", 'ac', "ad"]
for i in L:
    print("list : ".join(str(lst)
          for lst in L), " L = {0}".format(L), end="\n")

jourSemaine = ["lundi", "mardi", "mercredi",
               "jeudi", "vendredi", "samedi", "dimanche"]
for i in jourSemaine:
    print(jourSemaine)
print("il exists {0} jours dans une semaine".format(len(jourSemaine)))
print("sous liste ", jourSemaine[:-2:2])
print("dernier jour ", jourSemaine[-1])
print("en inverse ", jourSemaine[::-1])

# method 2
curr_date = date.today()
print(calendar.day_name[curr_date.weekday()])
# count nb occurence of spomethign


S = [10, 20, 50, 25, 30]
S.sort()
print(S)
S.append(12)
print(S)
S.reverse()
print(S)
print("inddice de l\'element 25 est {0}".format(S.index(25)))
S.remove(50)
print(S)
print(S[1:3])
print(S[:2])
X = S[:]
print("Last element using negative index {0}".format(S[-1]))

t = 'bon',
print(type(t))
# list tuple set dict
X = {'a', 'b', 'c', 'd'}
Y = {'s', 'b', 'd'}
print('c' in X)
print('c' in Y)
print('c' in (X or Y))
print(X-Y)
print(Y-X)
print("X Union Y {0}".format(X.union(Y)))
print("X Intersect Y {0}".format(X.intersection(Y)))
print('a inter b {0}'.format(Y & X))
print('a union b {0}'.format(Y | X))

# same {} in dict and sets
chuiLa = {11, 3, 11, 3}
print(chuiLa)

# ex dict
natureElements = dict()
natureElements["Au"] = dict()
natureElements["Au"]["tempSpecs"] = dict()
natureElements["Au"]["tempSpecs"]["TE"] = 2970
natureElements["Au"]["tempSpecs"]["TF"] = 1063
natureElements["Au"]["electron"] = dict()
natureElements["Au"]["electron"][0] = 79
natureElements["Au"]["electron"][1] = 169.967

natureElements["Ga"] = dict()
natureElements["Ga"]["tempSpecs"] = dict()
natureElements["Ga"]["tempSpecs"]["TE"] = 2237
natureElements["Ga"]["tempSpecs"]["TF"] = 29.8
natureElements["Ga"]["electron"] = dict()
natureElements["Ga"]["electron"][0] = 31
natureElements["Ga"]["electron"][1] = 69.967
print(natureElements["Au"]["electron"][0])
print(natureElements)


Dc = {"au": {"te/tf": (2970, 1063), "z/a": (79, 169)}, "ga": {
    "te/tf": (2237, 29.8), "z/a": (31, 69)
}}
print(Dc)


# formatting user output
a = 100
b = 200
# f"{varname}" is the new format after 3.9 : fstrict formatting
print(f"a={a} b={b}")
print("a=", a, " b=", b, sep="")
print("a={0} b={1}".format(a, b))

# user input
x = input("Donner x : ", )
print(x)
print(type(x))
# input has a default type str


while(True):
    try:
        testvalue = 1
        x = int(input("saisir un entier"))
        if(x % 2 == 0):
            print(f"{x} est pair")
        else:
            print(f"{x} est impair")
        break
    except (ValueError):
        print("sauf si")
x = float(input("saisir un entier x "))
y = float(input("saisir un entier y "))

print(x, y)
if(x > y):
    print(f"{x} est supérieur à {y}")
elif(x < y):
    print(f"{x} est inférieur à {y}")
else:
    print(f"{x} est égal à {y}")
ch = input("Enter a string ")
n = int(input("enter an integer "))
print(ch*n)
# set() set decl
# {} dic decl
# loops
ch = "abc"
for i in range(len(ch)):
    print(ch[i], end=" ")
print()
for i in ch:
    print(i, end=" ")
print()

for i in [1, 2, 2]:
    print(i, end=" ")
print()

for i in (12, 5, 5):
    print(i, end=" ")
print()
for i in {12: 5, 5: "a"}:
    print(i)
