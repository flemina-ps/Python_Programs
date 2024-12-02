#Quadratic_equation

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
x=(b**2)-(4*a*c)
if x==0:
    x1=(-b)/(2*a)
    print("There is only one solution")
    print(x1)
elif x>0:
    x2=-b+(x)/2*a
    x3=-b-(x)/2*a
    print("There are two solutions")
    print(x2,x3)
else:
    print("Solution is a complex number with real and imaginary value")
