class MinStack:


	def __init__(self):

		self.s = []

	def push(self, x):

		cur_min = self.getMin()
		if cur_min == None or x < cur_min:
			cur_min = x
		self.s.append((x, cur_min))	
	
	def pop(self):

		self.s.pop()

	def top(self):
		if not self.s:
			return None
		return self.s[-1][0]	

	def getMin(self):

		if not self.s:
			return None
		return self.s[-1][1]		

class MinStack:

	def __init__(self, s):
		self.s = []

	def push(self, x):
		if cur_min == None or x < cur_min:
			cur_min = x
		self.s.append((x, cur_min))	

	def pop(self):
		self.s.pop()

	def top(self):
		if not self.s:
			return None
		return self.s[-1][0]
	
	def getMin(self):
		if not self.s:
			return None
		return self.s[-1][1]						

