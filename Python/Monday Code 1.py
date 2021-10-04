amt=5800
li=[]
d={100:2, 200:3, 500:10}
amt=5800
n=0
print("Enter pin for ATM")
k=int(input())
c=0
if(k==1864):
	while(n<3):
    	c=0
    	print("Enter the amount to be withdrawn :")
    	w=int(input())
    	p=w
   	ninty=(90/100)*5800
    	if(w>amt):
        	print("Insufficient Balance")
        	break
   	if(w>ninty):
        	print("Transaction cannot be completer. Withdrawl amount more than 90%")
        	break
    	else:
        	fiven=w//500
        	c=c+(fiven*500)
        	of=d.get(500)
        	nf=of-fiven
        	if(nf<0):
            	print("Amount cannot be withdrawn")
            	break            
        	d.update({500:nf})
        	w=w%500
        	twon=w//200
        	c=c+(twon*200)
        	ot=d.get(200)
        	nt=ot-twon
        	if(nt<0):
            	print("Amount cannot be withdrawn")
            	break   
        	d.update({200:nt})
        	w=w%200
        	hund=w//100
        	c=c+(hund*100)
        	oh=d.get(100)
        	nh=oh-hund
        	if(nh<0):
            	print("Amount cannot be withdrawn")
            	break   
        	d.update({100:nh})
        	w=w%100
        	print("Amount withdrawn")
        	li.append(c)
        	n=n+1
    	amt=amt-p
else:
	print("Enter Pin again")
	c+=1
if(c==2):
	print("Account Blocked")
	
print("The transactions are: ")   
print(li)
print("The left over currency notes are: ")
print(d)
print("The new account balance: ")
print(amt)

        
