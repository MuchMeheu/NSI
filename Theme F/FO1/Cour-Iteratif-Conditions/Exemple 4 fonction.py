def somme_pairs(n):
    """
    n - int,entier positif ou nul
    Sortie:int- la somme des entiers pairs compris entre 0 et n
    """
    assert isinstance(n,int) or isinstance(n,float),"probleme de type"
    somme=0
    
    for i in range(0,n+1,2):
        somme=somme+i    

    return somme

