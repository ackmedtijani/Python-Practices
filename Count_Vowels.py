import re
string = eval(input("Enter the string: "))
def count_vowels(string):
	Pattern = re.compile(r'[aeiouAEIOU]')
	Message = Pattern.findall(string)
	count = 0
	for i in Message:
		count += 1
	return count

print(count_vowels(string))