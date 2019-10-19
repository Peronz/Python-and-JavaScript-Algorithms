class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left == None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			if data > self.data:
				if self.right == None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				data = self.data

	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data)
		if self.right:
			self.right.printTree()	

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left == None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			if data > self.data:
				if self.right == None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				data = self.data

	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.data)
		if self.right:
			self.right.printTree()											

			



