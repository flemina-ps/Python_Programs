#Pattern in the shape of a right angled triangle

#Right-Triangle
# n=int(input("Enter the limit : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#Inverted Right-Triangle
# n=int(input("Enter the limit : "))
# for i in range(1,n+1):
#     for j in range(i,n+1): #for i in range(n,i-1,-1)
#         print("*",end=" ")
#     print()


#Two right -triangles combined
# n=int(input("Enter the number : "))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print("*",end=" ")
#     print()
# for i in range(2,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#Two right-triangles combined in number pattern

n=int(input("Enter the limit : "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(2,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

