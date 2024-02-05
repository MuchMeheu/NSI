

#######################################Exercice 7######################################################

def rectangle(a,b,c):
    """
    a,b,c; des entiers strictement positifs
    sortie: Bool
    """
    assert not isinstance(a,str) and not isinstance(b,str) and not isinstance(c,str),"probleme type"
    assert a>0 and b>0 and c>0,"probleme positif"    
    if (a**2==b**2+c**2)or (b**2==a**2+c**2) or (c**2==a**2+b**2):
        return True
    return False
    

def isocele(a,b,c):
    """
    a,b,c; des entiers strictement positifs
    sortie: Bool
    """
    assert not isinstance(a,str) and not isinstance(b,str) and not isinstance(c,str),"probleme type"
    assert a>0 and b>0 and c>0,"probleme positif"
    
    if a==b and a!=c and b!=c or b==c and a!=c and b!=c or c==b and c!=a and b!=a:
        return True
    

def equilateral(a,b,c):
    """
    a,b,c; des entiers strictement positifs
    sortie: Bool
    """
    assert not isinstance(a,str) and not isinstance(b,str) and not isinstance(c,str),"probleme type"
    assert a>0 and b>0 and c>0,"probleme positif"
    
    if a==b==c:
        return True


#  programme principal
a= int(input ("donner la longueur du premier coté: "))
b= int(input ("donner la longueur du deuxième coté: "))
c= int(input ("donner la longueur du troisième coté: "))
assert (a<=b+c) and (b<=c+a) and (c<=a+b), "Attention "

#  ecrire ici un assert pour verifier que x, y et z peuvent former reellement un triangle: proporiete vue en 6eme 5 eme en maths
assert rectangle(3,4,5)==True
assert isocele(3,4,4)==True
assert equilateral(5,5,5)==True
print("Tests corrects")

if rectangle(a,b,c) and isocele(a,b,c):
    print ("Le triangle est rectangle isocele")
elif rectangle(a,b,c):
    print ("Le triangle est rectangle ")
elif isocele(a,b,c):
    print ("Le triangle est isocele ")
elif equilateral(a,b,c):
    print ("Le triangle est equilateral ")
else :
    print ("Le triangle est quelconque ")