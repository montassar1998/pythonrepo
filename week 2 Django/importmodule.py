""" 
from fichepersonne import * 
import  fichepersonne
import fichepersonne as fp 
from fichepersonne import A 
 """
#from mypoackage.module import fct

# pip install django
from math import ceil, floor, trunc

x = 1.4
y = 2.6

# floor x>0 x else x-1
# ceil x+1 if x > 0 else x

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
