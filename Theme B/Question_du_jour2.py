"""
Creer une listee de 10 entiers generees d'une maniere aleatoire par comprehension
"""

#methode 1
from random import *
liste=[randint(0,100)for i in range(10)]
print(liste)

#methode 2
L=[]
for i in range(10):
    L.append(randint(0,100))
print(L)
    