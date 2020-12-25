n=int(input())
i=2
while i<n :
    if n%i==0 :
        count=0
        print("n=",n,"not prime")
        break ;
    else :
        i=i+1
        if i==n:
            print("n=","it is prime")
