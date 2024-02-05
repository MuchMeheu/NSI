def carreparfait(n):
    "n est un nombre entier >=0"
    "Sortie:True or False:"
    assert isinstance(n,int),"probleme type"
    assert n>=0,"entre un nombre positif"
    for i in range(n+1):
        if i**2==n:
            return True
    return False

assert carreparfait(4)==True
assert carreparfait(5)==False
print("Tests corrects")
        
