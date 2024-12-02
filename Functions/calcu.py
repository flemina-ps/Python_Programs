#Sample calculator using functions
def calculator(n1,n2):
    print("Select the option number from the following")
    print("1 : Addition \n2 : Subtraction \n3 : Multiplication \n4 : Division \n5 : Exponent ")
    choice=int(input("Enter the option number: "))
    if choice==1:
        c=a+b
        return(f"The sum of two numbers {a} and {b} is {c}")
    elif choice==2:
        if n1<n2:
            n1,n2=n2,n1
        c=a-b
        return(f"The difference between two numbers {a} and {b} is {c}")
    elif choice==3:
        return(f"The product of two numbers {a} and {b} is ",a*b)
    elif choice==4:
        if b==0:
            return("Division by Zero is not possible")
        else:
            return(f"The quotient when two numbers {a} and {b} get divided is {c}")
        c=a/b
    elif choice==5:
        c=a**b
        return(f"The exponent of {a} raised to {b} is {c}")
    else:
        return("No valid option selected")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(calculator(a,b))
