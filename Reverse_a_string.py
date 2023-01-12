import re
string = str(input("Enter the string: "))
def main(s):
	x = len(s)
	string2 = ""
	for i in range(x-1 , -1 ,-1):
		string2 = string2 + s[i]
	return string2
def Reverse(string):
	Pattern = re.compile(r'\w+')
	Message = Pattern.findall(string)
	strings = ""
	for i in Message:
		strings = strings + main(i) + " "
	return strings
print(Reverse(string))