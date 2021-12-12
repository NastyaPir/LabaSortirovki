import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,10000))
kolsraw=0
kolperest=0
for i in range(0,len(a)-1):
    for j in range(i,len(a)):
        kolsraw=kolsraw+1
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            kolperest=kolperest+1
print(kolsraw,' ',kolperest)         