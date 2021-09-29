l=[["surbhi","surbhi@gmail.com",31123],["sejal","sejal@gmail.com",132312],
   ["akanksha","abs@gmail.com",52312],["auav","garav@gmail.com",43212]]

with open('sample.txt','w') as file:
    for i in l:
        file.write(str(str(i)+"\n"))

file2=open('sample.txt','r')
file2.read()
