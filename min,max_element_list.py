# find min and max element from a list along wid its index in list .
lst = eval(input("enter list :"))
length = len(lst)
min_ele = lst[0]
max_ele = lst[0]
min_index = 0
max_index = 0
for n in range(1, length):
    if lst[n] < min_ele:
        min_ele = lst[n]
        min_index = n
print("Given list is : ", lst)
print("The minimum element of the given list is : ")
print(min_ele, "at index", min_index)
for n in range(1, length-1):
    if lst[n] > max_ele:
        max_ele = lst[n]
        max_index = n
print("Given list is : ", lst)
print("The maximum element of the given list is : ")
print(max_ele, "at index", max_index)
