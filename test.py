def removeDuplicates(A):

	b = set()

	for a in A:
		if a not in b:
			b.add(a)
	return b		
		
print(removeDuplicates([1,1,2,3,2,1,3]))	


