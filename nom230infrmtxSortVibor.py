import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,10000))
min=a[0]
nom=0
kolsraw=0
kolperest=0
for j in range(0,len(a)-1):
    min=a[j]
    for i in range(j+1,len(a)):
        kolsraw=kolsraw+1
        if a[i]<min:
            min=a[i]
            nom=i
    a[j],a[nom]=a[nom],a[j]
    kolperest=kolperest+1        
print(kolsraw,' ',kolperest)
         