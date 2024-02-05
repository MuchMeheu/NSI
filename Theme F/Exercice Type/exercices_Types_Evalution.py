
# # # # # # # # # # # #  exercice 1  # # # # # # # # #
''' écrire une fonction python qui retourne le produit de tous les nombres compris entre 1 et n (inclus)
n doit être supérieur ou égal à 1. Dans ce programme, vous devez utiliser la boucle while.
'''

def produit(n):
    # Docstring  : compléter
    # Asserts    : compléter
    # Corps de la fonction : compléter
    """
    n entiers 
    sortie: Int
    """
    assert isinstance(n,int),"probleme type"
    assert n>=1,"probleme interval"
    resultat=1
    compteur=1
    while compteur<=n:
        resultat= resultat*compteur
        compteur=compteur+1
    return resultat
        
assert produit(3)==6
assert produit(5)!=121
print("test complets")




# # # # # # # # # # # #  exercice 2  # # # # # # # # #
''' Compléter la  fonction python suivante pour qu'elle retourne le nombre de multiples de 3 compris entre n et m inclus.
n et m etant les entrees de la fonction. Ils doivent etre entiers positifs et que n soit inferieur ou égal à m 

'''
def Nombre_multiples(n, m):
    '''
    n, m : int   n>=0 et m>=0 avec n<=m
    sortie: int, retourne le nombre de multiples de 3 compris entre n et m inclus. 
    '''
     
    assert isinstance(n,int) and isinstance(m,int),"probleme type"
    assert n>=0 and m>=0,"probleme signe"
    assert n<=m, "probleme n et m"
    compteur=0
    for i in range (n,m+1):
        if i%3==0:
            compteur= compteur+1
    
    return compteur
        
assert Nombre_multiples(1, 10) == 3
assert Nombre_multiples(1, 5) != 0 
print("tests 2 complets")




