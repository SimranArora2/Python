L1 = list(input())
print(L1)
element = input("Enter a string to be found =")
length = len(L1)
for n in range(0, length):
    if element == L1[n]:
        print(element, " string found at index ", n)
    break
else:
    print(element, " string not found ")
