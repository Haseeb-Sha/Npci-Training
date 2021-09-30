class project:
    project=["p1","p2","p3"]
class user(project):
    users=["u1","u2","u3"]  
    def operation(self):
        pro_user=["p1","P1","p2","P2","p3","P3"]   
        salary={"u3":5000,"u1":2000,"u2":3000}
        print(sorted(salary))
        lst_dct={pro_user[i]:pro_user[i+1] for i in range(0 , 6 ,2)}
        print(lst_dct)
ob=user()
print(ob.project)
print(ob.users)
ob.operation()
        
    