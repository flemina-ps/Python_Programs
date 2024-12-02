#Print the specific pattern
#*
# * +
# * + *
# * + * +
# * + * + *
# * + * + * +

n=int(input("Enter the number : "))
for i in range(1, n):
    for j in range(i):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print("+", end=" ")
    print()