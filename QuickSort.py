def quick_sort(left,right):
    global a,kolperest,kolsraw
    q=a[(left+right)//2]
    i=left
    j=right
    while i<j:
        kolsraw=kolsraw+1
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            kolperest=kolperest+1
        i+=1
        j-=1
    if left<j:
        quick_sort(left,j)
    if right>i:
        quick_sort(i,right)
    return(kolsraw,kolperest)                


import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,10000))
kolsraw=0
kolperest=0
left=0
right=len(a)-1
left,right=quick_sort(left,right)
print(kolsraw,' ',kolperest) 