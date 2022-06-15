# assert

# baseexception mother class of all exceptions
# under baseexception there is Exception
# under exception is all expceptions

# try except  finally except else

import code


try:
    x = int(input("saisir x"))
    print(1/x)
except ZeroDivisionError:
    print("erreur, Division par 0")
except ValueError:
    print("val")
else:
    print("pas d\'erreur")
finally:
    print("fixed")

# assert condition message ""
# assert is used in debugging
""" x=2
assert x!=2,"erreur val = 2 sans except" """
try:
    x = 2
    assert x != 2, "erreur val = 2 "
except:
    print("erreur assertion avec except")

try:
    raise Exception
except:
    print("raised exception manually")


def aff():
    # we use pass to define empty function or class
    pass


aff()
