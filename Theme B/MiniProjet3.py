"""
• fonction choix_mot (fonction qui choisit un mot dans une liste passée en paramètre.)
• fonction cacher_mot (fonction qui transforme un mot passé en paramètre en « * ».)
• fonction saisir_lettre (fonction qui demande à l’utilisateur de choisir une lettre.)
• fonction chercher_lettre (fonction qui cherche la lettre donnée par l’utilisateur dans le mot.)
• fonction remplacer_lettre (fonction qui remplace la lettre dans les « * » si elle appartient au mot.)



Le jeu devra comporter un :

 programme principal (qui fait appel aux fonctions précédentes)

Le jeu devra comporter une version 2 avec une :
 interface graphique (à l’aide de tkinter)


"""


from random import *
from tkinter import *

#fonction qui choisie un mot aleatorement dans la liste entree
def choix_mot(liste):
    """
    entree-  list de strings, avec les strings mots des miniscules
    sortie-  mot choisit, String
    """
    alphabet="abcdefghijklmnopqrstuvwxyzàâäéèêëîïôöùûüç"
    assert isinstance(liste, list),"Probleme type"
    for i in range(len(liste)):
        assert isinstance(liste[i], str),"Probleme type"
    for i in range(len(liste)):
        for element in liste[i]:
            assert element in alphabet, "entree dans la liste des mots minuscules"

    return choice(liste)

# Fonction qui transforme chaque caracteres du mot en asterisque pour le cache
def cacher_mot(mot):
    """
    entree-  le mot choisit, String
    sortie-  le mot cachee en « * », String
    """
    assert isinstance(mot, str),"Probleme type"
    motcache = ""
    for i in range(len(mot)):
        motcache += "*"
    return motcache

#Fonction qui fait saisir une lettre et qui regarde plusieurs criteres
def saisir_lettre():
    """
    entree- vide
    sortie- la lettre choisie
    """
    alphabet="abcdefghijklmnopqrstuvwxyzàâäéèêëîïôöùûüç"
    while True:
        lettre= str(input("Veuillez entrer une lettre: "))
        if lettre in alphabet and len(lettre) == 1:
            return lettre
        else:
            print("Veuillez Reessayer et entrer une seul lettre de l'aphabet minuscule")

#fonction qui cherche la lettre dans le mot
def chercher_lettre(mot,lettre):
    """
    entree: mot original et la lettre entree, str
    sortie: l'index de la lettre dans le mot original
    """
    indexlist=[]
    for i in range(len(mot)):
        if lettre ==mot[i]:
            indexlist.append(i)
            
    if indexlist==[]:
        return -1
    else :return indexlist

#fonction qui remplace la lettre dans le mot
def remplacer_lettre(index,lettre,motcache):
    """
    entree: l'index de la lettre, la lettre, le motcache , str
    sortie: le motcache modifier avec les lettres ajouter
    """
    mot_cache_liste = list(motcache)
    motcachemaj=""
    for i in range(len(mot_cache_liste)):
        if i in index:
            motcachemaj+=lettre
        else:
            motcachemaj+=mot_cache_liste[i]
    return motcachemaj
 
#fonction principale
def principale1():
    """
    entree: vide, fonction principale
    sortie: fin du programme
    """
    nbrtent = 0
    listeinput = input("Entrer une liste de mots séparés par des espaces pour commencer (sans guillemets) : ")
    liste_mots = listeinput.split()  
    motchoisit = choix_mot(liste_mots)
    motcache = cacher_mot(motchoisit)
    while '*' in motcache and nbrtent <= 7:
        lettre = saisir_lettre()
        index = chercher_lettre(motchoisit, lettre) 
        if index == -1:
            print("Cette lettre n'est pas dans le mot.")
            nbrtent += 1
        else:
            motcache = remplacer_lettre(index, lettre, motcache)
            if '*' not in motcache:
                print(f"Vous avez trouvé le mot {motchoisit} avec que {nbrtent} erreurs")
                return
    print(f"Vous avez rater, le mot était {motchoisit}.")










#Version 2

#fonction qui met a jour le mot cache 
def mettre_a_jour_mot(lettre):
    global mot_cache, mot_secret
    indices = chercher_lettre(mot_secret, lettre)
    if indices:
        mot_cache = remplacer_lettre(indices, lettre, mot_cache)

#fonction qui dessine le pendu d'apres la liste des etapes
def dessiner_pendu():
    global nombre_erreurs, etapes, dessin
    if nombre_erreurs < len(etapes):
        etape = etapes[nombre_erreurs]
        if etape[0] == "ovale":
            dessin.create_oval(*etape[1])
        else:
            for partie in etape:
                dessin.create_line(*partie)

#fonction qui change le mot cache dans l'interface pour le reveler
def mettre_a_jour_interface():
    global mot_cache, mot_secret, nombre_erreurs, mot
    mot["text"] = ' '.join(mot_cache)
    dessiner_pendu()
    if "*" not in mot_cache:
        afficher_victoire()
    elif nombre_erreurs >= limite_erreurs:
        afficher_defaite()

#fonction pour ecrire une victoire
def afficher_victoire():
    global info, boutons_lettres
    info["text"] = "Félicitations ! Vous avez gagné !"
    for bouton in boutons_lettres:
        bouton["state"] = DISABLED

#fonction pour afficher defaite
def afficher_defaite():
    global info, boutons_lettres, mot_secret
    info["text"] = f"Dommage... Le mot était '{mot_secret}'."
    for bouton in boutons_lettres:
        bouton["state"] = DISABLED

#fonction qui traite la lettre entree par l'utilisateur
def traiter_lettre(event):
    global nombre_erreurs
    bouton = event.widget
    lettre = bouton["text"]
    bouton["state"] = DISABLED
    if lettre not in mot_secret:
        nombre_erreurs += 1
        mettre_a_jour_interface()
    else:
        mettre_a_jour_mot(lettre)
        mettre_a_jour_interface()

#fonction qui initialise le jeu
def initialiser_jeu():
    global mot_cache, mot_secret, nombre_erreurs, liste_mots, boutons_lettres, dessin
    mot_secret = choix_mot(liste_mots)
    mot_cache = cacher_mot(mot_secret)
    nombre_erreurs = 0
    dessin.delete("all")
    for bouton in boutons_lettres:
        bouton["state"] = NORMAL
    mettre_a_jour_interface()

#inistialisation de l'interface graphique, des variables et de tous les boutons et text visuel 
def jeu_pendu_tkinter():
    global mot, info, dessin , boutons, boutons_lettres, bouton_rejouer,limite_erreurs, nombre_erreurs, liste_mots, etapes

    fenetre = Tk()
    titre = fenetre.title("Jeu du Pendu version Tkinter")

    limite_erreurs = 7
    nombre_erreurs = 0
    liste_mots = ["test","python","code","ethan","hadrien","mario","ilias","nsi"]

    mot = Label(fenetre, font=("Arial",20), fg="blue")
    mot.pack()

    info = Label(fenetre, font=('Arial', 14))
    info.pack()

    dessin = Canvas(fenetre, width=300, height=200)
    dessin.pack()

    boutons = Frame(fenetre)
    boutons.pack()

    boutons_lettres = []
    for lettre in "abcdefghijklmnopqrstuvwxyz":
        bouton = Button(boutons, text=lettre, font='times 15')
        bouton.pack(side=LEFT)
        bouton.bind("<Button-1>", traiter_lettre)
        boutons_lettres.append(bouton)

    bouton_rejouer = Button(fenetre, text="Rejouer", command=initialiser_jeu)
    bouton_rejouer.pack()

    etapes = [
        [(100, 180, 150, 180)],  
        [(125, 180, 125, 100)],  
        [(125, 100, 175, 100)],  
        [(175, 100, 175, 110)],  
        ["ovale", (170, 110, 180, 120)],  
        [(175, 120, 175, 150)],  
        [(175, 130, 165, 140), (175, 130, 185, 140)],  
        [(175, 150, 165, 160), (175, 150, 185, 160)]  
    ]

    initialiser_jeu()
    fenetre.mainloop()

# Choix de la version du jeu
def choisir_version():
    choix_version = input("Choisissez une version du jeu de pendu console ou tkinter 1 ou 2: ")
    if choix_version == "1":
        principale1()
    elif choix_version == "2":
        jeu_pendu_tkinter()
    else:
        print("Choix non valide. Veuillez entrer 'console' ou 'tkinter'.")


choisir_version()
