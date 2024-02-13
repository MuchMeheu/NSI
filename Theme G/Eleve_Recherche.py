from itertools import product
from string import ascii_uppercase as alphabet

"""
def lister_mots(l=3):

    return [''.join(lettres) for lettres in product(alphabet, repeat=l)]

mots5 =  lister_mots(3)

def recherche(Liste, A):
    compteur=0
    for element in Liste:
        compteur+=1
        if element==A:
            return (True, compteur)

print(recherche(mots5, 'NSI'))

#NSI trouver en 9265
#EULER trouver en 2186982

def recherche(Liste, A):
    debut = 0
    fin = len(Liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        element = Liste[milieu]

        if element == A:
            return (True, milieu + 1)

        if element < A:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return (False, -1)


def recherchedico(valeur,liste):
    inf=0
    compteur=0
    sup=len(liste)-1
    while inf<=sup:
        milieu=(inf+sup)//2
        compteur+=1
        if liste[milieu]==valeur:
            return True,compteur
        elif liste[milieu]<valeur:
            inf=milieu+1
        else:
            sup=milieu-1

print(recherchedico(3437,[23,36,34,236,75,4,53,231,23,353,5464,636,44234,213,2312,4326,3437,645233,14,647,5857,97,875,465,454,234,]))
print (recherchedico("NSI",mots5))


"""

def indice_min_depuis(liste, indice):
    indice_min = indice
    for i in range(indice, len(liste)):
        if liste[i] < liste[indice_min]:
            indice_min = i
    return indice_min

def tri_selection(liste):
        for i in range(len(liste)):
            mini = i
            for j in range(i+1, len(liste)):
                if liste[j] < liste[mini]:
                    mini = j
            liste[i], liste[mini] = liste[mini], liste[i]
        return liste