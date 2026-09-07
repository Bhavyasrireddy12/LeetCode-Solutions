class Solution:
    def distinctSubseqII(self, s: str) -> int:
        count=1
        mod=10**9+7
        last=[0]*26
        for ch in s:
            idx=ord(ch)-ord('a')
            old_count=count
            count=(2*count-last[idx]) % mod
            last[idx]=old_count
        return (count - 1) % mod 
        