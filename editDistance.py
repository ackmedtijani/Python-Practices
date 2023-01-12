''' Program to find the minimum number of operations to change 
String A to String B using operations: modify, delete, and insert
using dynamic programming'''

def main(A , B , m , n):
	if A[m - 1] == B[n - 1]:
		main(A , B , )
	else:
		return max(edx(main(A , B , ))