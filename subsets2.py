class ClassName:
	def sub(nums):
		if not nums:
			return []
		

		res = [[]]
		for i in range(len(nums)):
			for num in res[:]:
				res.append(num + [nums[i]])
		return res 

