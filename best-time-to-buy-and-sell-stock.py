class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxp=0
        minn=prices[0]
        for i in range(n):
            minn=min(minn,prices[i])
            profit=prices[i]-minn
            maxp=max(maxp,profit)
        return(maxp)
                
        
