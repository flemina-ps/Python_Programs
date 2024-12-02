# #Checking a user input in a list
# a=[]
# n=int(input("Enter the number of elements needed to the list : "))
# for i in range(0,n):
#     a1=int(input(f"Enter the number-{i+1} : "))
#     a.append(a1)

# print("Main List",a)
# count=0
# n1=int(input("Enter the number to be checked : "))
# for i in a:
#     if i==n1:
#         count+=1
# print(n1,"occured",count,"times")


# Check the index of a user input element
a=[]
n=int(input("Enter the total number of elements in the list : "))
for i in range(0,n):
    a1=int(input(f"Enter the number {i+1} : "))
    a.append(a1)
print("Main List ",a)
n1=int(input("Enter the number to be checked : "))
for i in a:
    if n1==i:
        print(a.index(i))
# print(i,"occured at the",index,"th index")





