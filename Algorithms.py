''' Question 1 '''

x  = int(input("Enter your integer: "))
y = int(input("Enter your second integer: "))

total = x + y
print("Total : "  , total)


''' Question 2 '''
odd = 0
even = 0
for i in range(0 , 4):
	x = int(input("Enter an integer: "))
	if x % 2 == 0:
		even += 1
	else:
		odd += 1

print("Number of even numbers: " , even)
print("Number of odd numbers: " , odd)

total = 0
count = 1
x = eval(input("Enter a number(integer or float: "))
while x != -88:
	x = eval(input("Enter a number(integer or float): "))
	total += x
	count += 1

print("The average of %i is %f" % (count , total/count))
