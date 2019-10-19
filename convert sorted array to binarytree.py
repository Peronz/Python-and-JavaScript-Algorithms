class Solution:
	def sortedArray(self, num):
		if not num:
			return None

		mid = len(num) // 2

		root = TreeNode(num[mid])
		root.left = self.sortedArray(num[:mid])
		root.right = self.sortedArray(num[mid+1])

		return root	