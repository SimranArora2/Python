# find an element from a list .
lst = eval(input("enter list :"))
length = len(lst)
element = int(input("enter a element to be searched for :"))
for n in range(0, length-1):
    if element == lst[n]:
        print(element, "found at index", n)
