x=5
y=6
i=input()
if i=="sum":
    sum=lambda x,y:x+y
    print(sum(x,y))
if i=="subtract":
    subtract=lambda x,y:x-y
    print(subtract(x,y))
if i=="multi":
    multi=lambda x,y:x*y
    print(multi(x,y))
if i=="divide":
    divide=lambda x,y:x//y
    print(divide(x,y))
ls=[]
print("Enter no of  values in list")
n=int(input())
for i in range (n):
    a=input()
    ls.append(a)
print("inputted list",ls)

lst_dct={ls[i]:ls[i+1] for i in range(0 , n ,2)}
print("list converted to dict",lst_dct)

for i in sorted (lst_dct):
    print(i,lst_dct[i])
su
    