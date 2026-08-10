class Solution:
    def winnerSquareGame(self, n: int) -> bool:
            dp=[False]*(n+1)
            for i in range(1,n+1):
                for j in range(1,i+1):
                    sqr=j*j
                    if sqr > i:
                        break
                    if dp[i-sqr]==False:
                        dp[i]=True
                        break
            return dp[n]                
       


        