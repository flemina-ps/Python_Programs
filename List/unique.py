#Find all unique elements from a list (elements appearing only once)
a=[]
a1=int(input("Enter the max count of elements in list : "))
for i in range(0,a1):
    a2=input(f"Enter the number {i+1} in list_1 : ")
    a.append(a2)
print("List : ",a)
u=[]
for i in a:
    if i not in u:
        u.append(i)
print("List of unique elements : ",u)