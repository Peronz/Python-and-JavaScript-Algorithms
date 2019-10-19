	

def a(self, head):
	slow, fast, pre = head, head, None
	while fast and fast.next:
	    pre, slow, fast = slow, slow.next, fast.next.next
	pre.next = None

def a(self ,head):
	a, b, c = head, head, None

	while b and b.next:
		c, a, b = a, a.next, b.next.next
	a.next = None
	
def a(self, head):
	a, b, c = head, head, None

	while b and b.next:
		c, a, b = a, a.next, b.next.next
	a.next = None				