class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            ans=0
        else:
            ans=n-1000+1  
        return ans