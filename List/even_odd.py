#count the number of even and odd numbers in a list
a=[]
a1=int(input("Enter the max count of elements in list_1 : "))
for i in range(0,a1):
    a2=int(input(f"Enter the element {i+1} in list_1 : "))
    a.append(a2)
e=[]
o=[]
even=0
odd=0
for i in a:
    if i%2==0:
        even+=1
        e.append(i)
    else:
        odd+=1
        o.append(i)
print("List : ",a)
print("The number of even numbers in the list : ",even)
print("The even numbers in the list are ",e)
print("The number of odd numbers in the list : ",odd)
print("The odd numbers in the list are ",o)


