class ArrayStack():
	def __init__(self):

		self._data = []

	def __len__(self):
		return len(self._data)

	def push(self , e):
		self._data.append(e)

	def top(self):

		if len(self._data) == 0:
			raise Empty('Stack is empty')

		return self._data[-1]

	def pop(self):
		if len(self._data) == 0:
			raise Empty('Stack is empty')
		return self._data.pop()

	def view(self):
		return self._data



