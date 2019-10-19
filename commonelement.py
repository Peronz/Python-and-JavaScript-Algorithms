def common(arr1, arr2):

	a = []

	for i in range(len(arr1)-1):
		for j in range(len(arr2)-1):
			if arr2[j] == arr1[i]:
				a.append(arr2[j])
	print(a)			
	return a
	
common([1, 3, 4, 5], [1, 4, 9, 8])													

