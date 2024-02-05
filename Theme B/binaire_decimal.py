def bindec(binaire):
    """
    entree: nombre en binaire
    sortie: nombre en decimal
    """
    assert isinstance(binaire,str),"Probleme type"
    assert len(binaire) >0, "attention votre chaine est vide"
    for element in binaire:
        assert element== "0" or element=="1", "attention ce ne sont pas des 0 ou des 1"
    decimal=0
    for i in range(len(binaire)-1,-1,-1):
        if i=="1":
            decimal+=2**i
    return decimal
    
print(bindec("1010"))

#correction 

def binaire_2_decimal(nb):
    """
    nb: str: ecriture binaire d'un entier positif
    sortie: int
    """
    decimale=0
    puissance = 0
    for i in range(len(nb)-1,-1,-1):
        decimale=decimale+int(nb[i]) *2 **(puissance)
        puissance=puissance+1
    return decimale

print(binaire_2_decimal("1010"))


def ecriture_binaire(decimale):
    """
    nb: entier positif
    sortie: une chaine de caractères
    """
    binaire=""
    while decimale!=0:
        if decimale%2==0:
            binaire+="1"
            decimale=decimale/2
        elif decimale%2==1:
            binaire+="1"
            decimale=decimale/2
    return binaire

def ecriture_binaire2(nb):
    """
    nb: entier positif
    sortie: une chaine de caractères
    """
    if nb==0:
        return "0"
    chaine=""
    while nb!=0:
        chaine= str(nb%2)+chaine
        nb=nb//2
    return chaine

print(ecriture_binaire2(15))
        
