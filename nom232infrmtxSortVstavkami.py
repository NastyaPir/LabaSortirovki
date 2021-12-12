import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,10000))
kolsraw=0
kolperest=0
for i in range(1,len(a)):
    k=a[i]
    nom=i
    while nom>0 and a[nom-1]>k:
        a[nom]=a[nom-1]
        kolperest=kolperest+1
        nom=nom-1
        if nom!=i:
            a[nom]=k
            kolsraw=kolsraw+1
print(kolsraw,' ',kolperest)    