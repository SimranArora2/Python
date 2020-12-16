nterms = 10
n1 = 0
n2 = 1
count = 0
tup = ()
# Check if the number of terms is valid !
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto , 'nterms':")
    while count < nterms:
        nup = tup+(n1,)
        nth = n1+n2
       # Update values .
        n1 = n2
        n2 = nth
        count = +1
        print(tup)
