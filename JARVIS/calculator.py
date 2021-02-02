def sum1(a,b) :
    c=a+b
    return c

def sub1(a,b) :
    c=a-b
    return c

def product1(a,b) :
    c=a*b
    return c

def div1(a,b) :
    c=a/b
    return c

def power1(a,b) :
    #c=a**b
    c= pow(a,b)
    return c

def root_any_integer(a,b):
    c=(pow(a,(1/b)))
    return c

while True:
    a = int(input("Enter first num : "))
    b = int(input("Enter second num : "))
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Exponential Calculation")
    print("6 for Root Calculation")
    o = int(input("Which operatioon do you want to perform ? "))
    
    if o == 1 :
        print(sum1(a,b)) 
    elif o == 2 :
        print(sub1(a,b))
    elif o == 3 :
        print(product1(a,b))
    elif o == 4 :
        print(div1(a,b))
    elif o == 5 :
        print(power1(a,b))
    elif o == 6 :
        print(root_any_integer(a,b))
    else :
        print("Enter Valid operator !!!")
    print("Enter 9 to quit else enter anything")
    user_input=int(input())
    if user_input==9:
        break
