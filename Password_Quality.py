import re
x = eval(input("Enter the value"))

def Password(x):

    Pattern = re.compile(r'''(([a-z]+[A-Z]+[0-9]+){8,})''',re.VERBOSE)
    Message = Pattern.search(x)
    if Message == None:
    	print()
    	print('Password must be 8 characters long')
    	print('Must have at least 1 Uppercase , 1 lowercase , 1 digit')
    else:
    	print()
    	print('Strong Password')

Password(x)

#Unfinished
