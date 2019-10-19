class Solution:
	def ismiror(self, p, q):
		if p == None and q == None:
			return True
		elif p == None or q == None:
			return False
		else:
			a = (p.val == q.val)
			return self.ismiror(p.left, q.right) and a and self.ismiror(p.right, q.left)
	def isSymmetric(self, root):
		if root == None or (root.left == None and root.right == None):
			return True
		return self.ismiror(root.left, root.right)					