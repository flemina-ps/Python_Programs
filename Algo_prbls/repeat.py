#Find the first character in a string that does not repeat
s = input("Enter the string: ")
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

non_repeating = 0
for char in s:
    if char_count[char] == 1:
        non_repeating = char
        break
if non_repeating:
    print("The first non-repeating character is:", non_repeating)
else:
    print("There are no non-repeating characters.")
