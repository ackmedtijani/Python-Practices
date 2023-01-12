def stalls(n):
	lists = []
	for i in range( 1 , n+ 3):
		if ((i == 1) or (i == n + 2)):
			lists.append(1)
		else:
			lists.append(0)
	return lists

print(stalls(4))