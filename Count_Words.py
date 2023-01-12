import re
string = eval(input("Enter the string: "))
def count_words(string):
	Pattern = re.compile(r'\w+')
	Match = Pattern.findall(string)
	count = 0
	for i in Match:
		try:
			int(i)
			Match.remove(i)
		except ValueError:
			pass
	for i in Match:
		count += 1
	return count
print(count_words(string))