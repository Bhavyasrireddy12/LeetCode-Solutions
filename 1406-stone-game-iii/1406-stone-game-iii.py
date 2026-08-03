class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
            n=len(stoneValue)
            store={}
            def dp(i):
                if i >= n:
                    return 0
                if i in store:
                    return store[i]
                tot=0
                best=float('-inf')
                for k in range(3):
                    if i + k<n:
                        tot+=stoneValue[i+k]
                        best=max(best,tot-dp(i+k+1))
                store[i]=best
                return best
            diff=dp(0)
            if diff>0:
                return "Alice"
            elif diff<0:
                return "Bob"
            else:
                return "Tie"                 
                        
        