from typing import Counter


s1=input()
s2=input()
s3=input()
c1=Counter(s1)
c2=Counter(s2)
c3=Counter(s3)
print (c1)
print (c2)
print (c3)
if(c1==c2 and c1==c3):
    print("Anagram")
else:
    print("Not Anagram")    

