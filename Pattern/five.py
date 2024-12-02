#Print the specified pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# Get the number of rows for the top half of the pattern from the user
n = int(input("Enter the number of rows : "))

# Print the increasing part of the pattern
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Print the decreasing part of the pattern
for i in range(n-1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
