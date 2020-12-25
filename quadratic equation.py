print("ax**2+bx+c")
a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if d>0:
    print("real and unequal roots")
if d==0:
    print("real and equal roots")
if d<0:
    print("imaginary roots")
    r1=(-b-d)/2*a
    r2=(-b+d)/2*a
    print(r1,r2)
