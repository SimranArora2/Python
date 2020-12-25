n1=int(input("enter the range to be started"))
n2=int(input("enter the range to ne ended"))
sume=0
sumo=0
for n in range(n1,n2) :
    if n%2==0 :
       sume+=n
       print("sum of even",n,"is",sume)
    else :
        sumo+=n
        print("sum of odd",n,"is",sumo)
