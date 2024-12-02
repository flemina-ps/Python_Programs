#Adding Elements of lists 
def sum_Of_List(a):
    print("First List ",a)
    # print("Second List ",b)
    sum1=0
    for i in a:
        sum1+=i
    print("Sum of elements of the list is  ",sum1)
a=[1,2,3,4,5]
sum=[]
sum_Of_List(a)

#Unique_elements
# def uni_Elements(a):
#     print(set(a))

# a=[1,2,1,2,3,4,1,5,6,3,6,7,2]
# uni_Elements(a)

#even_odd
# def even_Odd(a):
#     e=[]
#     o=[]
#     even=0
#     odd=0
#     for i in a:
#         if i%2==0:
#             even+=1
#             e.append(i)
#         else:
#             odd+=1
#             o.append(i)
#     print("Main List",a)
#     print("Even numbers are ",e)
#     print("Odd numbers are",o)
# a=[1,2,3,4,5,6,7,8,9]
# even_Odd(a)

#Palindrome

#Check if a list is a palindrome
# def Palindrome(a):
#     r=a[::-1]
#     print("Reversed List : ",r)
#     if a==r:
#         print("The list is a Palindrome")
#     else:
#         print("The list is not a Palindrome")

# a=[]
# a1=int(input("Enter the max count of elements in list_1 : "))
# for i in range(0,a1):
#     a2=input(f"Enter the element {i+1} in list_1 : ")
#     a.append(a2)
# print("List : ",a)
# Palindrome(a)

        
#check if two list are equal

# def equal_Lists(a,b):
#     for i in a:
#         for j in b:
#             if i==j:
#                 flag=1
#             else:
#                 flag=0
#     if flag==1:
#         print("Lists are equal")
#     else:
#         print("Lists are not equal")
# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# equal_Lists(a,b)