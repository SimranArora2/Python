list1=eval(input())
l1=list(list1)
print(l1)
sumO=0
sumE=0
for n in range(0,len(l1)):
    if n%2==0 :
            sumE=sumE+int(l1[n])
    else :
        sumO=sumO+int(l1[n])
       
print("Sum of even indexes:",sumE)
print("Sum o oddd indexes:",sumO)
