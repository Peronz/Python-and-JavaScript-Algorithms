class Solution:
	def s(self, nums):
		a = nums[0]
		b = nums[0]
		for num in nums[1:]:
			a += num
			b = max(a,b,num)
			a = max(a, num)
		return b	