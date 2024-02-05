""""

stock = {'poires': 5,'pommes': 10, 'fraises':35}

for nom, num in stock.items():
    print(nom, '->',num)


stock={'poires': 5,'pommes': 10, 'fraises':35}
inventaire=""
for nom in stock.keys():
    inventaire = inventaire + nom + ", "
print(inventaire)

for num in stock.values():
    print(num)

for nom, num in stock.items():
    print(nom, '->',num)


print(stock)
del stock['fraises']
print  (stock)
valeur=stock.pop('pommes')
print(stock)
print(valeur)

"""


d={'nom':'Dupuis','prenom':'Jacques','age':30},
d = {'nom': 'Dupuis', 'prenom': 'Jacques', 'age': 30}
keys = list(d.keys())
print(keys)

values = list(d.values())
print(values)

d = {'nom': 'Dupuis', 'prenom': 'Jacques', 'age': 30}

for cle, valeur in d.items():
    print(cle, '->', valeur)

    phrase = f"{d['prenom']} {d['nom']} a {d['age']} ans"
    print(phrase)

print(d['prenom'], d['nom']," a " ,d['age']," ans")

d={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
d = {str(i): 0 for i in range(10)}

def comptage(texte):
    dic={element:texte.count(element) for element in texte}
    return dic





# Questionnaire dico exo


d={"Aladin":[12,15,17],"Nathalie":[15,13,16], "Robert":[13,15,11]}
def calculer_moyenne(d):
    for cle, valeur in d.items():
        somme = 0
        for note in valeur:
            somme += note
        moyenne = somme / len(valeur)
        d[cle] = round(moyenne,2)
    return d

print(calculer_moyenne(d))

etudiant={"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 , "etudiant_5" : 8 , "etudiant_6" :
14 , "etudiant_7" : 16 , "etudiant_8" : 12 , "etudiant_9" : 13 , "etudiant_10" : 15 , "etudiant_11" : 14 , "etudiant_12" : 9 ,
"etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 , "etudiant_16" : 7 , "etudiant_17" : 12 , "etudiant_18" : 15
, "etudiant_19" : 9 , "etudiant_20" : 17 }

def admissions(dico):
    etudiantsAdmis = {}
    etudiantsNonAdmis = {}
    for etudiant, notes in dico.items():
        if notes >= 10:
            etudiantsAdmis[etudiant] = notes
        else:
            etudiantsNonAdmis[etudiant] = notes
    return etudiantsAdmis,etudiantsNonAdmis

print(admissions(etudiant))


dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Sumsung": 22 , "Iphone": 9 , "Other": 13 }
dicTablette = {"Sumsung": 15 , "Other": 13}

dictionnaire = {}  
dictionnaire.update(dicPC)
dictionnaire.update(dicPhone)
dictionnaire.update(dicTablette)
print(dictionnaire)
