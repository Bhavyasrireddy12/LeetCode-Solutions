class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        ans=0
        for i in range(n):
            pushes=(i // 8) + 1
            ans+=pushes
        return ans    
        
        