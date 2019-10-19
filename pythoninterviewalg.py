def anagram(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()

	if sorted(s1) == sorted(s2):
		print True

anagram('dog', 'god')	

ili

def anagram(s1, s2):
	s1 = s1.replace(' ', '').lower()
	s2 = s2.replace(' ', '').lower()

	if len(s1) != len(s2):
		return False

	count = {}
	
	for letter in s1:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1

	for letter in s2:
		if letter in count:
			count[letter] -= 1
		else:
			count[letter] =1 

	for k in count:
		if count[k] != 0:
			return False
	return True			

	# two sums

def two(nums, k):
	if len(nums) < 2:
		return None

	seen = set()
	output = set()

	for num in nums:
		target = k - num

		if target not in seen:
			seen,add(num)
		else:
			output.add((min(num, target), max(num, target)))

	print('\n'.join(map(str, list(output))))	
	
	# max sum of the array

def largest(arr):
	if len (arr) == 0
		return None
	max_sum = current_sum = arr[0]	
	for num in arr[1:]:
		current_sum = max(current_sum + num, num)
		max_sum = max(current_sum, max_sum)

	return max_sum	


# given a string of words, reverse all the words

def a(s1):
	s1.split()

	return s1[::-1]


# is 1 array rotation of another - return True/False

def rotation(list1, list2):
	if len(list1) != len(list2):
		return False
	key = list1[0]
	key_index = 0

	for i in range(len(list2)):
		if list2[i] == key:
			key_index = i
	break
	
	if key_index == 0:
		return False

	for x in range(len(list1)):
		l2index = (key_index + x) % len(list1)

		if list1[x] != list2[l2index]:
			return False
	return True
	

# Common elements in two sorted arrays

def common(arr1, arr2):

	a = []

	for i in range(len(arr1)-1):
		for j in range(len(arr2)-1):
			if arr2[j] == arr1[i]:
				a.append([arr2[j]])
	
	return a
	
common([1, 3, 4, 5], [1, 4, 9, 8])													


# frequent count

def e(nums):
	
	a = {}

	for i in nums:
		if i in a:
			a[i] += 1
		else:
			a[i] = 1
		return max(a[i])		 






