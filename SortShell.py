def shell(a,kolsraw,kolperest):
    step=len(a)//2
    while step:
        for i,el in enumerate(a):
            kolsraw=kolsraw+1
            while i>=step and a[i-step]>el:
                a[i]=a[i-step]
                kolperest=kolperest+1
                i=i-step
            a[i]=el
        step=1 if step==2 else int(step*5.0/11)
    return(a,kolsraw,kolperest)


import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,10000))
kolsraw=0
kolperest=0
a,kolsraw,kolperest=shell(a,kolsraw,kolperest)
print(kolsraw,' ',kolperest)