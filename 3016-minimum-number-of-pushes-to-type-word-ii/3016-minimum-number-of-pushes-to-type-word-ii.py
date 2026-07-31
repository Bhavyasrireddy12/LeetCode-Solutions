from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=sorted(Counter(word).values(),reverse=True)
        pushes=0
        ans=0
        for i in range(len(freq)):
            pushes=(i // 8) + 1
            ans+=freq[i] * pushes
        return ans    
        