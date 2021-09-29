s={2,5,6,7,3,3,3,3,7,34,6}
l=list(s)
for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if(l[j]<l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp

print(l)