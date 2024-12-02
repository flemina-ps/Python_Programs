#Reverse of a list without built-in methods
# a=[]
# n=int(input("Enter the max limit of the list : "))
# for i in range(0,n):
#     num=input(f"Enter the element {i+1} : ")
#     a.append(num)
# print("Main List",a)
# print("Reversed List : ",a[::-1])

#Method_2
a=[]
n=int(input("Enter the max limit of the list : "))
for i in range(0,n):
     num=input(f"Enter the element {i+1} : ")
     a.append(num)
print("Main List",a)
r=[]
for i in a:
     r.insert(0,i)
print(r)

