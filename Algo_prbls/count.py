# Compress a string such that consecutive characters are replaced with a single character followed by its count.

# i/p aaabbccca
# o/p:- a3b2c3a1
# Input string
s = "aaabbccca"
compressed = []
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1




















#     else:
#         # Append the character and its count to the result
#         compressed.append(s[i - 1] + str(count))
#         count = 1  # Reset count for the new character

# # Add the last character and its count
# compressed.append(s[-1] + str(count))

# # Join the list into a compressed string
# result = ''.join(compressed)

# # Output the result
# print("Compressed string:", result)
