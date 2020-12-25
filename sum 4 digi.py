n=int(input("enter the 4 digit number :"))
d1=n//1000
n=n-1000*d1
d2=n//100
n=n-100*d2
d3=n//10
n=n-10*d3
d4=n//1
d=d1+d2+d3+d4
print("the sum of the digits is :",d)
