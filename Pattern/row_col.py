#Pattern with equal rows and columns. user input

n=int(input('Enter the limit : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()