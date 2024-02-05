"""
1.
for i in range(5):
    for j in range(i,5):
        print(j, end=" ")
    print()
    
Reponse:
0 1 2 3 4 
1 2 3 4 
2 3 4 
3 4 
4
a chaque boucle j il va comment a une valeur i en moins commencant de 0 a 4


2."""
1.

for i in range(5):
    for j in range(i,5+i):
        print(j, end="")
    print()
    i=i+j
    

        

    
