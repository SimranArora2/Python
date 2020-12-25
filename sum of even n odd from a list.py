sumO=int(input())
sumE=int(input())
list=[5,3,11,12,15,0,13,17]
for n in range(0,len(list)):
      if n%2!=0:
          print(list[n])
          sumO =sumO+list[n]
          if n%2==0:
              print(list[n])
              sumE =sumE+list[n]
print(sumO)
print(sumE)
