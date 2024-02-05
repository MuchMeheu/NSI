'''

nombre =int(input("choisir un nombre:"))

if nombre%2 ==0:
    print("votre nombre est pair")
else:
    print("votre nombre est impair")

    


from math import *
nombre=int(input("choisir un nombre"))

if nombre>0:
    racine = sqrt(nombre)
    print("La racine carree de votre nombre est:", racine)
    
else:
    print("votre nombre doit etre positif")
    


a, b = int(input("choisir nombre a: ")),int(input("choisir nombre b: "))

if (a>0 and b>0) or (a<0 and b<0):
    print("podruit positif")
elif a==0 or b==0:
    print("produit nul")
else:
    print("produit negatif")
   



from random import *
a=randint(0,100)
print(a)
if a>50:
    print("votre nombre est inferieur a 50")
else:
    print("votre nombre est superieur a 50")

'''