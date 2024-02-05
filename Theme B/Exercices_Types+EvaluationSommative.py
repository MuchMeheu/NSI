#Écrire une fonction en Python qui prend en parametres une chaine de caracteres et qui renvoie un dictionnaire dont les clés 
# sont les caractères de la chaine saisie et les valeurs sont les positions des caractères dans la chaine. si le caractere se repete, 
# la fonction renvoie l'indice le plus grand. 
def position(chaine):
    """
    chaine – char, une chaine de caractere non vide 
    Sortie: dictionnaire – contenant les positions des caractères dans la chaine.
            En cas de plusieurs occurences d'un caractere, on renvoie l'indice le plus grand de ce caractere dans chaine. 
    >>>position('chainee')
    {c:0 , h : 1 , a: 2 , i: 3, n:4 , e: 6 }
    """
    d = {}
    for i in range(len(chaine)):
        d[chaine[i]] = i
    return d
print(position('chainee'))

    
    
    

#Écrire une fonction en Python qui prend en parametre un texte(phrase) et qui renvoie un dictionnaire dont les clés sont les mots du texte
# saisi et les valeurs sont les longueurs des mots qui composent le texte. 
# Rappel
# Convertir le texte T en une liste
#liste_words = T.split()

def analyse(texte):
    """
    chatexteine – char, une chaine de caractere non vide 
    Sortie: dictionnaire – contenant la longueur de chaque mot du texte.
            
    >>>analyse("Python est un langage de programmation" )
    {'Python' : 6, 'est': 3, 'un': 2, 'langage': 7, 'de': 2 , programmation : 13 }
    """
    d = {}
    lmots = texte.split()
    for element in lmots:
        d[element] = len(element)
    return d

print(analyse("Python est un langage de programmation" ))