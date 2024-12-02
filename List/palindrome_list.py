#Check if a list is a palindrome
a=[]
a1=int(input("Enter the max count of elements in list_1 : "))
for i in range(0,a1):
    a2=input(f"Enter the element {i+1} in list_1 : ")
    a.append(a2)
print("List : ",a)
r=a[::-1]
print("Reversed List : ",r)
if a==r:
    print("The list is a Palindrome")
else:
    print("The list is not a Palindrome")

    
