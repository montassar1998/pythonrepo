#no biblio , only module and package
#file in python with functions is a module
#multiple files in a folder are a package
#import package.module 
#import package.module.entity
import math, random, os
# class with internal class
class Dept:
    def __init__(self, dname) -> None:
        self.dname = dname
    # relation d'appartenance

    class Prof:
        def __init__(self, pname) -> None:
            self.pname = pname


math = Dept("mathematics")
mathprof = Dept.Prof("Mark")
print(math.dname)
print(mathprof.pname)


class person:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom


class student(person):
    def __init__(self, nom="anon", prenom="anony") -> None:
        super().__init__(nom, prenom)
    pass


P = person("X", "Y")
print(hasattr(P, "nom"))
print(hasattr(P, "prenom"))
print(hasattr(P, "age"))


s = student()
print(issubclass(student, person))
print(issubclass(person, student))


print(isinstance(P, person))
print(isinstance(s, person))

