class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        maxp=0
        for i in range(len(prices)-1):
            j=i+1
            if(prices[i]<prices[j]):
                p=prices[j]-prices[i]
                maxp+=p
        return(maxp)
        
