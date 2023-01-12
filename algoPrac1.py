# Fibonacci sequence using dynamic programming


import time


def fib(n):
	table = [None] * (n + 1)
	def main(n):
		if not table[n]:
			if n <= 1:
				table[n] = 1 
				return 1
			table[n] = main(n - 1) + main(n - 2)
			return table[n]
		return table[n]
	main(n)
	return table[n - 1]

start = time.time()
print(fib(5))
stop = time.time()
elapsed_time = stop- start
print(elapsed_time)