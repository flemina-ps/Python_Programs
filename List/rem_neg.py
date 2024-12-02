#Remove all negative numbers from a list
a=[]
a1=int(input("Enter the max count of elements in list : "))
for i in range(0,a1):
    a2=input(f"Enter the number {i+1} in list_1 : ")
    a.append(a2)
print("List : ",a)
n=[]
for i in a:
    if i>=0:
        n.append(a[i])
print("List after removing negative numbers : ",n)