class person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __afficher(self):
        print(f"{self.fname}:{self.lname}:{self.age}")

    def __str__(self):
        return self.fname+" "+self.lname+" "+str(self.age)


p = person("montassar", "riahi", 24)
# a method to call a 'private' method inside a main module
p._person__afficher()
#overriding the function __str__()
print(p)
