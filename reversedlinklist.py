class Solution:
	def a(head):

		prev = None
		curr = head

		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		return prev
		
class Solution:
	def reverse(self, head):
		return self.re(head)
	def re(self, curr, prev=None):
		if not curr:
			return None

		temp = curr.next
		curr.next = prev

		return self.re(temp, curr)	
