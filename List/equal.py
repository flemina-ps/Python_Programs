#Check if two lists are equal (same elements in the same order)
a=[]
b=[]
a1=int(input("Enter the max count of elements in list_1 : "))
for i in range(0,a1):
    a2=input(f"Enter the element {i+1} in list_1 : ")
    a.append(a2)

b1=int(input("Enter the max count of elements in list_2 : "))
for i in range(0,b1):
    b2=input(f"Enter the element {i+1} in list_2 : ")
    b.append(b2)

for i in a:
    for j in b:
        if i==j:
            flag=1
        else:
            flag=0
if flag==1:
    print("Lists are equal")
else:
    print("Lists are not equal")
