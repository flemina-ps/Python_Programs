a=[]
a1=input("Enter the max count of elements in list : ")
for i in range(0,a1):
    a2=input(f"Enter the {i+1} element in list: ")
    a.append(a2)
print("List : ",a)
b=input("Enter the sublist to be checked: ")
count=0
if b in a:
    print(b,"occured",count,"times")
else:
    print("No substring present")