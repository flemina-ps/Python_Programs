# Function to Print Fibonacci Series up to n Terms
def fib(i):
    if i <= 1:
        return i
    else:
        return (fib(i - 1) + fib(i - 2))

num=int(input("Enter the limit: "))
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fib(i))