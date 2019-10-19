def zigzagLevelOrder(self, root):
	if not root:
		return []
	reverse = False
	nodes = [root]
	ret = []
	while nodes:
		vals = [node.val for node in nodes]
		if reverse:
			vals = vals[::-1]
		ret.append(vals)
		nodes = [kid for node in nodes for kid in (node.left, node.right) if kid]
		reverse = not reverse
	return ret			