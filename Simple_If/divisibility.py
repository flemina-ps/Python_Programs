#Checking if a number is divisible by both 5 and 11

n=int(input("Enter the number: "))
if n%5==0 and n%11==0:
        print(f"The number {n} is divisible by both 5 and 11")
else:
    print(f"The number {n} is not divisible by both 5 and 11")
