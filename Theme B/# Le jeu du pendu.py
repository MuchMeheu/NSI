from tkinter import *

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



def dessiner_pendu(canvas, nbr_erreurs):
    etapes = [
        canvas.create_line(100, 180, 150, 180),  # Base
        canvas.create_line(125, 180, 125, 100),  # Poteau vertical
        canvas.create_line(125, 100, 175, 100),  # Poteau horizontal
        canvas.create_line(175, 100, 175, 110),  # Corde
        canvas.create_oval(170, 110, 180, 120),  # Tête
        canvas.create_line(175, 120, 175, 150),  # Corps
        [canvas.create_line(175, 130, 165, 140),  # Bras gauche
                 canvas.create_line(175, 130, 185, 140)], # Bras droit
        [canvas.create_line(175, 150, 165, 160),  # Pied gauche
                 canvas.create_line(175, 150, 185, 160)]  # Pied droit
    ]

    if nbr_erreurs < len(etapes):
        etape_actuelle = etapes[nbr_erreurs]
        if isinstance(etape_actuelle, list):
            for action in etape_actuelle:
                action()
        else:
            etape_actuelle()

def principale2():
    def demarrer_jeu():
        mots_saisis = entree_mots.get().strip().split()
        if mots_saisis:
            global motchoisit, motcache
            motchoisit = choix_mot(mots_saisis)
            motcache = cacher_mot(motchoisit)
            label_mot.config(text=motcache)
            cadre_saisie.pack_forget()  # Cache le cadre de saisie des mots

    def mise_a_jour_jeu():
        global nbrtent, motcache
        lettre = entree_lettre.get().strip().lower()
        entree_lettre.delete(0, END)  # Effacer la saisie après chaque soumission

        if not lettre or len(lettre) > 1 or lettre not in "abcdefghijklmnopqrstuvwxyzàâäéèêëîïôöùûüç":
            messagebox.showinfo("Erreur", "Veuillez entrer une seule lettre valide.")
            return

        index = chercher_lettre(motchoisit, lettre)
        if index != -1:
            motcache = remplacer_lettre(index, lettre, motcache)
            label_mot.config(text=motcache)
            if "*" not in motcache:
                messagebox.showinfo("Gagné", f"Félicitations! Vous avez trouvé le mot {motchoisit}.")
                fenetre.destroy()
        else:
            nbrtent += 1
            dessiner_pendu(canvas, nbrtent)
            if nbrtent >= 7:
                messagebox.showinfo("Perdu", f"Dommage! Le mot était {motchoisit}.")
                fenetre.destroy()

    fenetre = Tk()
    fenetre.title("Jeu du Pendu")

    # Cadre pour la saisie des mots
    cadre_saisie = Frame(fenetre)
    cadre_saisie.pack()

    label_explication = Label(cadre_saisie, text="Entrez les mots séparés par des espaces :")
    label_explication.pack()

    entree_mots = Entry(cadre_saisie, width=50)
    entree_mots.pack()

    bouton_demarrer = Button(cadre_saisie, text="Démarrer le jeu", command=demarrer_jeu)
    bouton_demarrer.pack()

    label_mot = Label(fenetre, text="* * * * *")
    label_mot.pack()

    entree_lettre = Entry(fenetre)
    entree_lettre.pack()

    canvas = Canvas(fenetre, width=300, height=200)
    canvas.pack()

    bouton_soumettre = Button(fenetre, text="Soumettre", command=mise_a_jour_jeu)
    bouton_soumettre.pack()

    # Initialisation des variables globales
    global motchoisit, motcache, nbrtent
    motchoisit = ""
    motcache = ""
    nbrtent = 0

    fenetre.mainloop() 



def choisir_version():
    choix = input("Tapez '1' pour la version console ou '2' pour la version Tkinter : ")
    if choix == '1':
        principale1()
    elif choix == '2':
        principale2()
    else:
        print("Choix invalide. Veuillez entrer '1' ou '2'.")

choisir_version()