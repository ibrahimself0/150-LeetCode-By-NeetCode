class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits = [0]
        length = len(prices) - 1
        i = length
        j = length
        while (i>=0):
            j=i
            while(j>=0):
                print(prices[i] - prices[j])
                profits.append(prices[i] - prices[j])
                j-=1
            i-=1        
        print(profits)
        if(max(profits)>0):
            return max(profits)
        else:
            return 0    
