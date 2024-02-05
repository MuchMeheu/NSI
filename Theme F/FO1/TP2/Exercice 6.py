def premier(n):
    "n est un nombre entier >=0"
    "Sortie:True or False:"
    assert isinstance(n,int),"probleme type"
    assert n>=0,"entre un nombre positif"
    if n==1: return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

assert premier(7)==True
assert premier(10)==False
print("Tests corrects")
        