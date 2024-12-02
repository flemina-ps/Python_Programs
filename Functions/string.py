#Function to Check if a String is a Palindrome
def is_palindrome(s):
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
    return s
n=input("Enter the string: ")
print(is_palindrome(n))