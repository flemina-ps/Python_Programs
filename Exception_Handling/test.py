# try:
#     num1=int(input("Enter the first number : "))
#     num2=int(input("Enter the second number : "))
#     res=num1/num2
#     print(f"The quotient of {num1}/{num2} is {res}")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# finally:
#     print("Finally Block")

# a = [10, 20, 30]
# i = 3
# try:
#     print(a[i])
# except IndexError:
#     print("Index is out of range. Please check your list.")


def sum_Of_Two(a,b):
    s=a+b
try:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    s=a+b
    sum_Of_Two(a,b)
except ValueError:
    print("Invalid value entered")
else:
    print(f"The sum of numbers {a} and {b} is {s}")
finally:
    print("Code Executed")