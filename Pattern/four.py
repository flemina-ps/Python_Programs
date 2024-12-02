# #Print a specific pattern
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
# 2 4 6 8 10 12

r=int(input("Enter the number of rows : "))
for i in range(1,r+1):
    for j in range(1,i+1):
            print(2*j,end=" ")
    print()