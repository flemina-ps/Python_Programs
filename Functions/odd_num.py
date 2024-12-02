#Print odd numbers from one to n using function
def is_odd(n):
    i=1
    while i<n:
        if i%2==1:
            print(i)
        i+=1
n=int(input("Enter the limit : "))
is_odd(n)

