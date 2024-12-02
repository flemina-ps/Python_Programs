#sum_of_two_list
limit=int(input("Enter the number of elements : "))
a=[]
b=[]
sum=[]
for i in range(0,limit):
    a1=int(input(f"Enter the  element {i+1} in the first list : "))
    a.append(a1)
for i in range(0,limit):
    b1=int(input(f"Enter the  element {i+1} in the second list : "))
    b.append(b1)
print("First List ",a)
print("Second List ",b)
for j in range(0,limit):
    sum1=a[j]+b[j]
    sum.append(sum1)
print("Sum of elements of first and second list ",sum)