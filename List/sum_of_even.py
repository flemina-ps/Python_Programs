#Find the sum of all even numbers in a list
a=[]
a1=int(input("Enter the max count of elements in list : "))
for i in range(0,a1):
    a2=int(input(f"Enter the number {i+1} in list_1 : "))
    a.append(a2)
print("List : ",a)
s=[]
sum=0
for i in a:
    if i%2==0:
        s.append(i)
print("The even numbers in the list are : ",s)
for j in s:
    sum+=j
    j+=1
print("Sum of all even numbers in the list are : ",sum)

