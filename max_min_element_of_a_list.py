my_list = []  # list
print("enter five integers")
for i in range(5):
    print("enter integer%d=" % i, end="")
    userinput = int(input())
    my_list.append(userinput)
print("the list is:", my_list)
max1 = my_list[0]
for n in range(1, 5):
    if max1 < my_list[n]:
        max1 = my_list[n]
print(max1)
min1 = my_list[0]
for n in range(1, 5):
    if min1 > my_list[n]:
        min1 = my_list[n]
print(min1)
