import random


class cube:
    def __init__(self):
        self.__numFace = 0

    def __str__(self):
        return f'{self.__numFace}'

    def lancerDe(self):
        self.__numFace = random.randint(1, 6)

    def getValeurDe(self):
        return self.__numFace


class personne:
    def __init__(self):
        self.nom = input("saisir le nom ")
        self.prenom = input("saisir le prenom ")
        self.age = int(input("saisir l\'age "))

    def __str__(self) -> str:
        return f' nom = {self.nom} prenom = {self.prenom} '


class joueur(personne):

    def __init__(self, c1=cube(), c2=cube()):
        # name, age and last name will be input in the person class constructor
        super().__init__()
        self.d1 = c1
        self.d2 = c2
        self.score = 0

    def jouer(self):
        self.d1.lancerDe()
        self.d2.lancerDe()
        return self.d1.getValeurDe() + self.d2.getValeurDe()

    def __str__(self) -> str:
        return f" => score = {self.score} d1 = {self.d1.getValeurDe()} d2 = {self.d2.getValeurDe()} " + super().__str__()


joueur1 = joueur(cube(), cube())
joueur2 = joueur(cube(), cube())
while (True):

    if(joueur1.jouer() > joueur2.jouer()):
        joueur1.score += 10
    else:
        joueur2.score += 10
    print(joueur1)
    print(joueur2)
    if(joueur2.score >= 100):
        print("Jouerur 2 a gagné ")
        print(joueur2)
        break
    elif (joueur1.score >= 100):

        print("Joueur 1 a gagné")
        print(joueur1)
        break
