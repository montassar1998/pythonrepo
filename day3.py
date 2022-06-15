from pprint import pprint


(lambda ch: print(ch))("Bonjour je suis une fonction lambda")

# iterables are types like list...

l = [20, 8, 3, 87]
Map = list(map(lambda x: x+1, l))
print(Map)


def filterFunction(x):
    return True if x > 10 else False


Fl = list(filter(filterFunction, l))
print(Fl)

# file system in python
firstFile = open("file.txt", "a+")
firstFile.write(input("saisir le contenu du fichier"))
firstFile.write("\n")
firstFile.close()
""" try:
    with open("Gcp.jpg", "rb") as f:
        byte = f.read(1)
        while byte:
            # Do stuff with byte.
            byte = f.read(1)
            print(byte)
except IOError:
     print('Error While Opening the file!')   """


# activity
def saisie():
    nom = ""
    while (nom == ""):
        nom = input("saisir un nom ")
    prenom = ""
    while(prenom == ""):
        prenom = input("saisir un prenom")
    tp = ""
    while True:
        try:
            tp = float(input("saisir une note entre 0 et 20 TP "))
        except ValueError:
            continue
        if(tp >= 0 and tp <= 20):
            break
    Exam = ""
    while True:
        try:
            Exam = float(input("Saisir une note examen entre 0 et 20 "))
        except ValueError:
            continue
        if(Exam <= 20 and Exam >= 0):
            break
    return nom, prenom, tp, Exam


def moy(student):
    return 0.4*student[-2]+0.6*student[-1]


Note = open("Note.txt", "a+")
n = 0
while(True):
    try:
        n = int(input("Saisir le nombre d\'eleves "))
    except:
        continue
    if(0 < n < 6):
        break
for i in range(n):
    student = saisie()
    print(student)

    avg = moy(student)
    print(avg)
    for j in student:
        Note.write(str(j) + " ")
    Note.write(str(avg)+'\n')
    # student[i]....


Note.close()


NoteOpen = open("Note.txt", "r+")
k = NoteOpen.readlines()
classAvg = 0
for i in k:
    x = i.split(" ")
    classAvg+= float(x[-1])
    if(float(x[-1]) >= 12):
        print(f"mois de 12 {i}")
print(f'the class average is {classAvg/len(k)}')