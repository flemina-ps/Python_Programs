#Print sum of n numbers using recursion
def sum(n):
    if n<=1:
        return 1
    else:
        return n+sum(n-1)
n=int(input("Enter the limit : "))
print(f"Sum of numbers from 1 to {n} is",sum(n))
