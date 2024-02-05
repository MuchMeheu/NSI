def val_abs(x):
    """
    x-int ou float
    Sortie: int ou float- la valeur absolue de x
    """
    assert isinstance(x,int) or isinstance(x,float),"probleme de type"
    if x<0:
        x=-x
    return x

assert val_abs(100)==(100)
assert val_abs(-100)==(100)
print("Tests corrects")
