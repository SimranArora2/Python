x = eval(input("Enter a list : "))
def reverse(seq):
    temp = []
    while seq:
        temp.append(seq.pop())
    seq[:] = temp
 
reverse(x)
print("Reversed list : ",x)