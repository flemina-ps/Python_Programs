# #Function syntax
# def sum():
#     a=12
#     b=1
#     c=a+b
#     return c
# print(sum())

# #Using parameters
# def sum(a,b):
#     c=a+b
#     return c
# print(sum(1,3))

#User input
def sum(a,b):
    c=a+b
    return(f"sum of {a} + {b} = {c}")
    # print(f"sum of {a} + {b} = {c}")
n1=int(input("Enter  the number 1 : "))
n2=int(input("Enter the number 2: "))
print(sum(n1,n2))