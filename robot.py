class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'y = {self.y}  x = {self.x}'
    #overriding the + operator
    def  __add__(self,otherPoint):
        return point(self.x+otherPoint.x, self.y + otherPoint.y)
# composition


class robot:
    Version = 0
    name = ""

    def __init__(self,  name="Apollo", p=point(0, 0), orientation="Nord"):
        self.__orientation = orientation
        print(__name__)
        self.__pos = p
        robot.Version += 1
        robot.name = name

    def getCoords(self):
        return (self.__pos.x, self.__pos.y)

    def setCoords(self, newX, newY):
        self.__pos.x = newX
        self.__pos.y = newY

    def setDirection(self, newDir):
        if (not newDir in ["Nord", "West", "East", "South"]):
            print("Invalid direction")

        else:
            self.__orientation = newDir

    def getDirection(self):
        return self.__orientation

    def turnRight(self):
        ref = ["Nord", "East", "South", "West"]
        print(ref.index(self.__orientation))
        self.__orientation = ref[(ref.index(self.__orientation)+1) % 4]
        pass

    def avancer(self):



        if(self.__orientation == "Nord"):
            self.__pos.y += 1
        elif (self.__orientation == "South"):
            self.__pos.y -= 1
        elif(self.__orientation == "East"):
            self.__pos.x += 1
        else:
            self.__pos.x -= 1

    def __str__(self) -> str:

        return f"{self.__orientation} version = {robot.Version} name = {robot.name}   call : "+str(self.__pos.x) + f" {self.__pos.y} "


# r = robot("Hyper", 4, 5, "W")
# r.setCoords(10, 6)
# r.setDirection("U")
# r.getUpdatedCoords("k")
# print(r.getDirection())
# r.setDirection("South")
# print(r.getDirection())
# print(r.getCoords())
p1 = point(1,2)
p2 = point(4,4) 
print(p1+p2)
vers = input("Saisir une version ")
name = input("Saisir le nom de votre robot ")
R1 = robot(name)
# R1.Version = vers
# print(R1)
# R1.setDirection("Nord")
# R1.avancer()
# R1.setDirection("East")
# R1.avancer()

print(R1)

while(True):
    n = (input("Voulez vous tournez O/N"))

    if(n == "O"):
        R1.turnRight()

    n = (input("Voulez vous avancer O/N"))
    if(n == "O"):
        R1.avancer()
    print(R1)

