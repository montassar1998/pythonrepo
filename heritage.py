class student:
    D = dict()
    id = 1

    def __init__(self, fname, lname):
        self.nom = fname
        self.prenom = lname
        self.__note1 = 0
        self.__note2 = 0
        self.__note3 = 0
        student.id += 1

    def saisieNote(self):
        self.__note1, self.__note2, self.__note3 = float(
            input("note 1")), float(input("note 2")), float(input("note 3"))

    def __str__(self) -> str:
        print(f"{self.nom} {self.prenom} {self.__note1} {self.__note2} {self.__note3}")

    def enregistrer(self):
        dct = dict()
        dct["prenom"] = self.prenom
        dct["N1"] = self.__note1
        dct["N2"] = self.__note2
        dct["N3"] = self.__note3
        student.D[self.id] = dct
        print(student.D)

    def taille():
        return len(student.D)
    def averageGrade():
        sum = 0
        for i in student.D.keys():
            sum+=float(student.D[i]['N3'])
        return sum/len(student.D)


x = student("m", "r")
print(student.id)
x.saisieNote()
x.enregistrer()

y = student("a", "b")
print(student.id)
y.saisieNote()
y.enregistrer()

print(student.taille())
print(student.averageGrade())



