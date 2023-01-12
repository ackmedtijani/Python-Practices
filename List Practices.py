spam = ['apples','bananas','tofu','cats']
string = "";
def list(spam):
	for i in spam:
		string = string + str(spam[i])
	return string	
print(list())

