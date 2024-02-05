from random import randint

def creer_Aleatoire(nb_Lignes, nb_Colonnes):
    sous_ligne =[]
    matrice = []
    for i in range(nb_Lignes):
        sous_ligne = []
        for j in range(nb_Colonnes):
            sous_ligne.append(randint(0,100))
        matrice.append(sous_ligne)
    print(matrice)
    return matrice




def multiplier(matrice,valeur):
    for i in range(len(matrice)):
        for k in range(len(matrice[0])):
            matrice[i][k]= matrice[i][k]*valeur
            
    return matrice

print(multiplier(creer_Aleatoire(4,4),2))
    
        
        