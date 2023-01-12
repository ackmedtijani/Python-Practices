def check(n):
	return str(4) not in str(n)

def if_divisible(n):
	for divisor in [2 , 3 , 5,  7]:
		if n % divisor == 0:
			return True
	return False

def main(n , add = False):
	for divisor in [2 , 3 , 5 , 7]:
		quotient = n / divisor
		if check(quotient):
			difference = n - quotient
			if check(difference) and n % divisor == 0:
				if add:
					print("Case{0}: {1} {2}".format(t , quotient , difference - 1))
					break
				print("Case {0}: {1} {2}".format(t , quotient , difference))
				break



t = int(input())
for i in range(1 , t+1):
	n = int(input())
	if if_divisible(n):
		main(n)
	else:
		main(n+1 , add = True)

