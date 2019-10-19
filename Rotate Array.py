class Solution:
	def rotate(self, nums, k):

		numsCopy = nums[:]

		for i in range(len(nums)):
			nums[(i + k) % len(nums)] = numsCopy[i]