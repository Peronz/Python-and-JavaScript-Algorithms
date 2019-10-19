class Solution:
	def closestValue(self, root, target):

		return self.binary_search(root, target, root.val)

	def binary_search(self, root, target, closest):
		if not root: return closest
		if abs(root.val - target) < abs(closest - target):
			closest = root.val
		if root.val > target: 
			return self.binary_search(root.left, target, closest)
		else:
			return self.binary_search(root.right, target, closest)	
				