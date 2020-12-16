radius=int(input())
print("1.calculeate area")
print("2.calculate perimeter")
choice=int(input("enter the choice"))
if choice==1:
    area=3.14159*radius*radius
    print("area=",area)
else:
    peri=2*3.14159*radius
    print("perimeter=",peri)
