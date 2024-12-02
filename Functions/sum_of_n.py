#Print the sum of n natural numbers
def sum_of_n(n):
    i=1
    sum=0
    while i<=n:
        sum+=i
        i+=1
    print("Sum of natural numbers upto",n,"is",sum)
n=int(input("Enter the limit : "))
sum_of_n(n)


#arbitrary arguments
#arbitrary keyword arguments

