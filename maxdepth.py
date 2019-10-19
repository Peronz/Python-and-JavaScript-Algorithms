class Solution:
	def maxDepth(self, root):
		depth = 0
		level = [root] if root else []
		while level:
			depth += 1
			queue = []
			for el in level:
				if el.left:
					queue.append(el.left)
				if el.right:
					queue.append(el.right)
			level = queue
		return depth


class Solution:
	def maxDepth(self, root):
		depth = 0
		if root:
			level = [root]

		while level:
			depth += 1
			q = []
			for el in level:
				if el.left:
					q.append(el.left)
				if el.right:
					q.append(el.right)
			q = level
		return depth											