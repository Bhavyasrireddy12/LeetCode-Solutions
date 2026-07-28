class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        ans = prices[:]
        for i in range(len(prices)-1,-1,-1):
            while s and s[-1] > prices[i]:
                s.pop()
            if s:
                ans[i] = prices[i] - s[-1]
            s.append(prices[i]) 
        return ans           




        