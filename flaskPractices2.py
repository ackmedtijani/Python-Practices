''' Tidy numbers for small data samples '''

def leadingzero(n):
	lists = []
	for i in range(1 , n + 1):
		if '0' not in str(i):
			lists.append(i)

	return lists



def changetoint(y):
	lists = []
	for i in y:
		lists.append(int(i))
	return lists

def is_sorted(lists):
	for i in range(len(lists)-1):
		for j in range(1 ,len(lists)):
			if lists[i] > lists[j]:
				return False
	return True

def descendingorder(n):
    if len(str(n)) > 1:
    	lists = leadingzero(n)
    	list2 = []
    	for i in lists:
    		y = str(i)
    		if (len(y) > 1):
    			x = changetoint(y)
    			if is_sorted(x):
    				list2.append(i)

    	return list2[len(list2) - 1]
    else:
        return n




print(descendingorder(256))