n1=int(input())
n2=int(input())
n3=int(input())
N=n1+n2+n3
if  n1==n2==n3: 
   print ("sum 2=",n1)
else :
    print ("sum 1=",n1+n2+n3)
if  n1==n2!=n3 :
    print ("sum 2=",n1+n3)
else :
    print ("sum 1=",n1+n2+n3)
if  n1!=n2!=n3:
    print ("sum 1=",n1+n2+n3)
else :
    print  ("sum 2=",n1+n2) or ("sum 2=",n1+n3) or ("sum 2=",n2+n3)
