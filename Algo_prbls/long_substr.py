# Find the Longest Substring Without Repeating Characters
# Initialize Variables:
# max_length: A variable to keep track of the length of the longest substring without repeating characters, initialized to 0.
# start: A variable to mark the start index of the current substring, initialized to 0.
# char_index: A dictionary to store the last seen index of each character.
# Iterate Over the String:
# Loop through each character in the string using enumerate to get both the index i and the character char.
# Check for Repeating Characters:
# If the current character char is already in char_index and its recorded index is greater than or equal to start, it means the character has appeared before within the current substring.
# Update start to char_index[char] + 1 to move past the previous occurrence and ensure no repeating characters are included.
# Update the Last Seen Index:
# Store the current index i of the character char in char_index.
# Calculate the Length of the Current Substring:
# Compute the length of the current substring as i - start + 1 and update max_length if this length is greater than max_length.
# Return the Result:
# After looping through the string, max_length will hold the length of the longest substring without repeating characters.
# s=input("Enter the string : ")
# max_length=0
# start=0
# char_index={}
# for i,char in enumerate(s):
#     if char in char_index and char_index[char] >= start:
#         start = char_index[char] + 1  
#     char_index[char] = i
#     max_length = max(max_length,i - start + 1)

# print("The length of the longest substring without repeating characters is:", max_length)


s=input("Enter the string : ")
max_length=0
start=0
char_index={}
for i in range(len(s)):
    char=s[i]
    if char in char_index and char_index[char] >= start:
        start = char_index[char] + 1  
    char_index[char] = i
    current_length=i-start+1
    if current_length>max_length:
        max_length=current_length
print("Length of the longest substring: ",max_length)
