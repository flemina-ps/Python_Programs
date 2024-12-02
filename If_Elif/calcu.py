#Calculator

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Select the option number from the following")
print("1 : Addition \n2 : Subtraction \n3 : Multiplication \n4 : Division \n5 : Exponent ")
n=int(input("Enter the option number: "))
if n==1:
    print(f"The sum of two numbers {a} and {b} is ",a+b)
elif n==2:
    print(f"The difference between two numbers {a} and {b} is ",a-b)
elif n==3:
    print(f"The product of two numbers {a} and {b} is ",a*b)
elif n==4:
    print(f"The quotient when two numbers {a} and {b} get divided is ",a/b)
elif n==5:
    print(f"The exponent of {a} raised to {b} is ",a**b)
else:
    print("No valid option selected")
   
