lst=[99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80]
slc1=lst[5:98]
slc2=lst[::96]
sum=avg=0
print("Slice 1")
for n in slc1 :
    sum+=n
    print(n , end=' ')
print()
print("Sum of elements of sclice 1:", sum)
print("Sclice2")
sum=0
for n in slc2 :
    sum+=n
    print(n , end=' ')
print ()
avg=sum/len(slc2)
print ("Average of elements of slice 2:" , avg)













