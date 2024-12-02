a=[]
n=int(input("Enter the number of elements : "))
for i in range(0,n):
    elements=int(input())
    a.append(elements)

odd=[]
even=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(a)
print("List of even numbers are",even)
print("List of odd numbers are",odd)
