class Solution:
	def levelOrder(self, root):
		if not root:
			return []
		q = deque()
		q.append(root)
		levels = []
		oneLevel = []

		while len(q) != 0:
			for i in range(len(q)):
				popped = q.popleft()
				oneLevel.append(popped.val)
				if popped.left:
					q.append(popped.left)
				if popped.right:
					q.append(popped.right)
			levels.append(oneLevel)
			oneLevel = []
		return levels	
