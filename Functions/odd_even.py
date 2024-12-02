# Function to Check if a Number is Even or Odd
def is_even_odd():
    x = int(input("Enter the number : "))
    if x % 2 == 0:
        return(f"{x} is an even number")
    else:
        return (f"{x} is an odd number")
print(is_even_odd())