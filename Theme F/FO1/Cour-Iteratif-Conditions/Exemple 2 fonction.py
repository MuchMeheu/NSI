def echange(a,b):
    """
    a,b-int ou float
    Sortie:int ou float- la valeur de a va dans b, celle de b va dans a,
            les nouvelles valeur de a et b sont renvoyee dans cet ordre.
    """
    assert (isinstance(a,int) and isinstance(b,int)) or (isinstance(a,float) and isinstance(b,int)),"probleme de type"
    a,b=b,a
    return (a,b)

assert echange(1,2)==(2,1)
assert echange(-2,-3)==(-3,-2)
print("Tests corrects")
