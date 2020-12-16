a=int(input("enter 1st no.:"))
b=int(input("enter 2nd no.:"))
c=int(input("enter 3rd no.:"))
if a==b and b<c :
      print(a,"=",b,"<",c)
elif a<b and b==c :
      print(a,"<",b,",",c)
elif a<b and b<c :
      print(a,"<",b,"<",c)
elif b<c and c<a :
      print(b,"<",c,"<",a)
elif c<b  and b<a :
      print(c,"<",b,"<",a)
elif a==c and c<b :
      print(a,",",c,"<",b)
else :
      a==b==c
      print(a,"=",b,"=",c)
   
