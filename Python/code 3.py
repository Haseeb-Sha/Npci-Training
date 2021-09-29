l=[["haseeb","123@gmail.com",31123],["prakahr","345@gmail.com",132312],
   ["suhail","abs@gmail.com",52312],["azaan","kbc\@gmail.com",43212]]

with open('sample.txt','w') as file:
    for i in l:
        file.write(str(str(i)+"\n"))

file2=open('sample.txt','r')
file2.read()
