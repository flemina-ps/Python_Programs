#Calculate SI using function with default argument
def simple_Interest(p,r,t):
    return (p*r*t)/100

p=int(input("Enter the principal amount: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time in years: "))
print("Simple Interest=",simple_Interest(p,r,t))