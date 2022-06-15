class A:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom

    def __str__(self) -> str:
        return f'{self.nom} {self.prenom}'


a = A("xx", "yy")
