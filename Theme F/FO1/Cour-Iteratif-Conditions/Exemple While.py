print("ce programme continue de s'executer jusqu'a ce que l' utilisateur saisisse 0")
saisie=int(input("votre choix:"))
compteur=0

while (saisie!=0):
    print("La table de multiplication de",saisie, "est:")
    for i in range(1,11):
        print(i,"*",saisie,"=",i*saisie)
    compteur=compteur+1
    saisie=int(input("votre choix: "))
    
print("vous avez cherchez la table de multiplication d'un chiffre :", compteur, "fois")
    
    

    
           