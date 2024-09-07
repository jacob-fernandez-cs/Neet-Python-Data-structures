class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #create two pointers, left is the day you buy right is the day you sell
        l, r = 0, 1
        maxProfit = 0

        #only move the left pointer if there is a smaller value in the list

        while r < len(prices):#while the right pointer has not reached the end of the list of prices
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r #if price[l] is < prices[r] that means a new low position has been found move the left pointer to the position of the right pointer
            r += 1
        return maxProfit

Solution = Solution()
list = [7,1,5,3,6,4]
print(Solution.maxProfit(list))