"""
Sujet 3
Ethan Vesic
Ilias Gaudineau
"""




from random import *
print("Le jeu du nombre mystere ")
print(" ")
print("Dans quel mode voulez-vous jouer ?")
print("1) L'ordinateur choisit le nombre")
print("2) L'utilisateur choisit le nombre")
mode=int(input("Votre choix: "))  #Choix du mode
print("==============================")

if mode==1: #mode ordinateur
    compteur=0
    a=randint(1,100)
    b=int(input("choix: "))
    while a!=b: #boucle continue jusqu'a que le nombre entrer = nombre choisie par l'ordinateeur
        if a>b:
            print("C'est plus grand!")
        else:
            print("C'est plus petit!")
        b=int(input("choix: "))
        compteur=compteur+1
    if a==b: #fin du jeux nombre trouve
        print("Bravo ! Vous avez trouve en",compteur,"coups !") 
        
        
    
    
elif mode==2: #mode utilisateur
    
    input("appuyer sur entrer quand vous avez choisie votre nombre...")
    a=False
    x=1
    y=100
    compteur=0
    while a==False: # continuation du jeu tant que a=False
        compteur=compteur+1
        val=randint(x,y)
        print("Je tent ma chance...",val,"!")
        print("1)C'est ca!")
        print("2)Plus petit")
        print("3)Plus grand")
        b=int(input("Choix: "))
        if b==1:   #ordinateur trouve la valeur
            a=True
        elif b==2: #la valeur donne est plus petite
            y=val
        elif b==3: #la valeur donne est plus grand
            x=val
    
    print("L'ordinateur a trouve en",compteur,"coups!") #fin du jeux


else:
    print("Reesaye et choisit une des option")