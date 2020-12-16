a1=int(input("enter number 1="))
a2=int(input("enter number2="))
a3=int(input("enter number 3="))
a4=int(input("enter number 4="))
a5=int(input("enter number 5="))
b=int(input("enter div ="))
no=0
if a1%b==0:
    no+=1
if a2%b==0:
    no+=1
if a3%b==0:
    no+=1
if a4%b==0:
    no+=1
if a5%b==0:
    no+=1
print("no",no)
