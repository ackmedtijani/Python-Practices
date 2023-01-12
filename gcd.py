''''Recursive algorithm for the greatest common denominator of 
      integers x and y '''



def gcd(x , y):
	if y == 0:
		return x
	else:
		gcd(y , x%y)


