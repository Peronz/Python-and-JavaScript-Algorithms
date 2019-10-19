def e(nums):
	
	count = {}
	max_count = 0
	max_item = None

	for i in nums:
		if i not in count:
			count[i] = 1

		else:
			count[i] += 1

		if count[i] > max_count:
			max_count = count[i]
			max_item = i
	print(max_item)		
	return max_item	

e([1,1,1,2])	
	


