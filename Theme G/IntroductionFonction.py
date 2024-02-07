
def maximum(Liste):
    Max=Liste[0]
    for element in Liste:
        if element>Max:
            Max=element
    return Max
print(maximum([3,6,84,23,5433,436,3]))

def minimum(Liste):
    Min = Liste[0]
    for element in Liste:
        if element < Min:
            Min = element
    return Min

print(minimum([3,6,84,23,5433,1,436,3]))


def moyenne(Liste):
    somme=0
    for element in Liste:
        somme+=element

    return somme/len(Liste)

print(moyenne([3,6,84,23,5433,1,436,3]))

def recherche(Liste, A):
    compteur=0
    for element in Liste:
        compteur+=1
        if element==A:
            return (True, compteur)
        
print(recherche([3,6,84,23,5433,1,436,3], 84))

