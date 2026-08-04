from functools import lru_cache
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            maxi=0
            ans=0
            for j in range(i,min(i+k,n)):
                maxi=max(maxi,arr[j]) 
                length=j-i+1
                ans=max(ans,maxi*length+dp(j+1))    
            return ans
        return dp(0)    