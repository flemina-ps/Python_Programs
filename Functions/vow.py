
# count of vowel in a string using set

def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for alphabet in str:
		if alphabet in vowel:
			count = count + 1
	print("No. of vowels :", count)

str = input("Enter the string : ")
vowel_count(str)
