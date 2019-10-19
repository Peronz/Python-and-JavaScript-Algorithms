def uniq(string):
	a = set()

	for i in string:
		a.add(i)
		if len(a) == len(string):
			return True
		else:
			return False


print(uniq('asfjafaf'))
