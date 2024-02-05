L=[5,-1,6,7,8]
print(L)
del L[1]
print (L)
L2=['B','c','d','z','r','w']
car=L2.pop(-1)
print(car)

l=[1,2,3,-4,0]
l2=[]
for i in range(len(L)-1,-1,-1):
    l2.append(l[i])
print(L2)