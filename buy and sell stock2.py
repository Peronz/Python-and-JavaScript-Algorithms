class Solution:
	def maxProfit(self, prices):
		if len(prices) == 0: return 0

		max_to_here = 0
		max_so_far = 0

		for i in range(1, len(prices)):
			max_to_here = max(0, max_to_here + prices[i] - prices[i-1])
			max_so_far = max(max_so_far, max_to_here)

		return max_so_far
		
		ili


	def maxProfit(self, prices):
		if len(prices) == 0:
			return 0

		min_price = prices[0]
		max_profit = 0

		for i in range(len(prices)-1):
			if prices[i] < min_price:
				min_price = prices[i]
			else:
				max_profit = max(max_profit, prices[i] - min_price)
		return max_profit				
