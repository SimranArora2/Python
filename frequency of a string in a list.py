L = input()
L1 = list(L)
print(L1)
length = len(L1)
element = input("enter the string")
count = 0
for i in range(0, length):
    if element == L1[i]:
        count += 1
print(count, "is frequency of string ")
