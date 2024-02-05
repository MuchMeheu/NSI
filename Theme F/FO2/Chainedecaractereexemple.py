"""
ville="Dubai"
lg=len(ville)
print(lg)

dernier_element=ville[-1]
print(dernier_element)

print(ville[0])

for i in range(lg):
    print(ville[i])
    
for element in ville:
    print(element)

nom="Laure LEGRAND"
print(nom[0:5])
print(nom[6:14])
print(nom[:14])
print(nom[6:len(nom)])
print(nom[6:])
"""

phrase="Ma joueuse de Tennis preferee est : Devinez!!"
print(phrase.lower())
print(phrase.upper())
print(phrase.swapcase())
print(phrase.title())
"""

def nombre_e(chaine):
    """
    #chaine-str (chaine de caracteres)
    #Sortie: int - le nombre de lettre <<e>> dns la chaine
    """
    for i in range(len(chaine)):
        if chaine[i]=='e':
            compteur=compteur+1
    return compteur


def rang_premier_e(chaine):
    """
    #chaine-str -chaine de caracteres
    #Sortie : int -le numbero de place du premier "e" dajs la chaine (la premiere place est numerotee 0)
    #Renvoie -1 s'il ny a pas de "e" dans la chaine
    """
    for i in range(len(chaine)):
        if chaine[i]=='e':
            return i
            
        else:
            return -1
            
def rang_premier_eV2(chaine):
    """
    #chaine-str -chaine de caracteres
    #Sortie : int -le numbero de place du premier "e" dajs la chaine (la premiere place est numerotee 0)
    #Renvoie -1 s'il ny a pas de "e" dans la chaine
    """
    indice =0
    for element in chaine:
        if element=='e':
           return indice
        
        else :
            indice+=1
    return -1

assert rang_premier_eV2('salut')==-1
assert rang_premier_eV2('est ce que tout va bien')==0
print('les tests sont corrects')
    
            

"""
def espacer(chaine):
    """
    chaine-str (chaine de caracteres
    sortie:str=la chaine dans laquelle un espace a ete insere entre chauqe letre
    """
    assert isinstance(chaine,str), "probleme de type"
    chaineespace=""
    for element in chaine:
        chaineespace= chaineespace +(element+" ")
    return chaineespace


def inverser(chaine):
    """
    chaine- str(chaine de caracteres)
    Sortie: str - ecriture "inversee" de cette chaine;
            le premier caractere devint le dernier
                    le duexieme devient l'avant dernier, etc...
    """
    assert isinstance(chaine,str),"pbr type"
    res=''
    for i in range(len(chaine)-1,-1,-1):
        res+=chaine[i]
    
    return res
    
    
def est_palyndrome(chaine):
    """
    chaine- str(chaine de caracteres)
    Sortie: bool- Vrai si la chaine de caractere est un palyndrome Faux si non
    """
    assert isinstance(chaine,str),"pbr type"
   
    res=''
    for i in range(len(chaine)-1,-1,-1):
        res+=chaine[i]
    if chaine==res:
        return True
    else:
        return False
        
assert est_palyndrome('salut')==False
assert est_palyndrome('radar')==True
print('les tests sont corrects')    

        
        
    
def nbr_voyelle(chaine):
    """
    
    
    """
    compteur=0
    voyelle='oieyau'
    for element in chaine:
        if element in voyelle:
            compteur=compteur+1
    return compteur

print(nbr_voyelle("anticonstitutionellement"))


def premiermot(chaine):
    """
    
    
    """
    res=''
    for element in chaine:
        if element==" ":
            return res
        else:
            res+=element


