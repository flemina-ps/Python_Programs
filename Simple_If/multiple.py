#Checking if a number is a multiple of 3 or 7

n=int(input("Enter the number: "))
if n%3==0 or n%7==0:
    print(f"The number {n} is a multiple of 3 or 7")
else:
    print(f"The number {n} is not a multiple of 3 or 7")
