from operator import itemgetter
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


class joueur:
    def setScore(self, newV):
        self.__score = newV

    def getScore(self):
        return self.__score

    def __init__(self, c1=cube()):
        # name, age and last name will be input in the person class constructor
        self.__d1 = c1

        self.pseudo = input("saisir votre pseudo : ")
        print(f"caller is {inspect.stack()[1][3]} ")
        dicts = toDictionnary("")
        #print(f"dicts = {dicts} {self.pseudo in dicts}")
        if (self.pseudo in dicts):
            for i in dicts.keys():
                if (i == self.pseudo):
                    self.__score = int(dicts[i])
        else:
            self.__score = 0
            ajouterScore(self.pseudo, 0, "")

        self.__chemin = [0]

    def avancer(self):
        self.__d1.lancerDe()
        turnValue = self.__d1.getValeurDe()
        #print(f"De {turnValue} {self.__chemin[-1]} ")
        fourBckwards = [5*i for i in range(1, 6)]
        twoForwards = [10*i for i in range(1, 6)]
        #print(f'{self.__chemin} {self.pseudo}')
        if (self.__chemin[-1]+turnValue <= 63):
            self.__chemin.append(self.__chemin[-1]+turnValue)
        if (self.__chemin[-1] in fourBckwards):
            self.__chemin.append(self.__chemin[-1]-4)
        if (self.__chemin[-1] in twoForwards):
            self.__chemin.append(self.__chemin[-1]+2)
        if(self.__chemin[-1] == 63):
            print(f"{self.pseudo} {self.__score} gagne! avec chemin {self.__chemin} ")
            self.__score += 10
            ajouterScore(self.pseudo, self.__score, "")
            return True

        #print(f'vous etes {self.pseudo} et vous etes sur  {self.__chemin}')
        return False

    def __str__(self) -> str:
        return f" => score = {self.score} d1 = {self.d1.getValeurDe()} " + super().__str__()


class jeu_de_table:
    # bug when we declare j1 = joueur() and j2 = joueur()
    # to be fixed
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2

    def jouer(self):
        while(True):
            t1 = self.j1.avancer()

            #print(f"SCORE joueur {self.j1.getScore()}{self.j2.getScore()} ")
            if(t1):
                print("Done !")
                break
            t2 = self.j2.avancer()
            if(t2):
                print("Done !")
                break


def pseudoExists(playerPseudo, f):
    # with open(filename, 'r', encoding='UTF-8') as file:
    # while (line := file.readline().rstrip()):
    #     print(line)
    f = open("players.txt", "r")
    lines = f.readlines()
    couple = zip(lines[0::2], lines[1::2])
    for i in couple:
        if(i[0].rstrip('\n') == playerPseudo):
            f.close()
            return True
    f.close()
    return False


def toDictionnary(f):
    f = open("players.txt", "r")
    lines = f.read()
    lines = lines.split("\n")
    D = dict()
    keys = lines[0::2]
    values = lines[1::2]

    for i, j in zip(keys, values):
        D[i] = j
    f.close()
    print("D=", D)
    return D


def saveDict(inputDict, f):
    f = open("players.txt", "w")

    for i in inputDict.keys():
        f.write(str(i)+'\n')
        f.write(str(inputDict[i])+'\n')
    f.close()


def ajouterScore(pseudo, score, f):
    f = open("players.txt", "r")

    lines = f.readlines()

    try:
        ind = lines.index(pseudo+"\n")
        #print("ind = ", ind)
    except ValueError:
        lines.append(pseudo+'\n')
        lines.append(str(score)+'\n')
    else:
        for i in range(0, len(lines), 2):
            if (lines[i].rstrip('\n') == pseudo):
                lines[i+1] = str(score)+'\n'
                print(f"line found  = {lines[i]} et sco {score}")
    for i in lines:
        i = i+'\n'
    f.close()
    f = open("players.txt", "w")
    f.writelines(lines)
    f.close()


def maxScore(f):
    f = open("players.txt", "r")
    lines = f.read()
    lines = lines.split("\n")
    convertedToInt = [int(i) for i in lines[1::2]]
    lines = list(zip(lines[0::2], convertedToInt))

    res = list(map(max, zip(*lines)))

    print(f" lines max = {res}")

    f.close()
    return res


f = ""
# f.seek(0,2) puts the cursor in the last position

# print(pseudoExists("kalthoum", f))
# newVal = toDictionnary(f)
# ajouterScore("p", "1340", f)
# newVal = toDictionnary(f)
# print("li", toDictionnary(f))
# newVal["hend"] = 1998
# saveDict(newVal, f)
# ajouterScore("hend", "2023", f)
# print(toDictionnary(f))
# maxScore(f)

print("player 1  :")
p1 = joueur()
print("player 2  :")
p2 = joueur()

game = jeu_de_table(p1, p2)
game.jouer()
