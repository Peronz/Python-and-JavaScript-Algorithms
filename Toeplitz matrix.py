class Solution:
	def a(self, matrix):
		for row in range(len(matrix)):
			for col in range(len(matrix[0])):
				if row>0 and col > 0 and matrix[row][col] != matrix[row-1][col-1]:
					return False
		return True		


class Solution:
	def mat(self, matrix):
		for row in range(len(matrix)):
			for col in range(len(matrix[0])):
				if row > 0 and col > 0 and matrix[row][col] != matrix[row-10][col-1]:
					return False
		return True			

