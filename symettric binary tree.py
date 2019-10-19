class Solution:
	def symmetric(self, root):
		if not root:
			return True
		return self.check(self, l, r):
	def check(self, l, r):
		if l and r:
			return l.val == r.val and self.check(l.left, r.right) and self.check(l.right, r.left)
		return l == r	
				