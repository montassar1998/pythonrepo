class personne:
    #static variable
    Id=0
    # # constructor with no parameters
    # def __init__(self):
    #     self.nom = "anonymous"
    #     self.prenom = "undefined"
    #     self.age = -1 
    # constructor with default valued parameters

    def __init__(self, n="anonymous", p="undefined", a="22"):
        self.nom = n
        self.prenom = p
        self.age = a
        personne.Id +=1

    def __str__(self):
        return f"{self.nom} : {self.prenom} : {self.age}\n"


P1 = personne("montassar", "riahi", 23)
P2 = personne("Azer", "saadallah", 24)
PA = personne()
PDef = personne("monta" )
print(P1, P2, PA, PDef,P1.Id, P2.Id)
