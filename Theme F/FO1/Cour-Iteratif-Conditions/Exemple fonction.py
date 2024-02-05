def Puis3(nb):
    """
    nb-flot(ou int)
    Sortie : float (ou int), le cube du nbr
    """
    #assertion pour verifier le type de nbr
    assert isinstance(nb,int) or isinstance(nb,float),"probleme de type"
    y=nb**3
    return y

assert Puis3(3)==27
assert Puis3(5)==125
print("les tests sont corrects")