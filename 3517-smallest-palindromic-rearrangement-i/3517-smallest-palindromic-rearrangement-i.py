from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq=Counter(s)
        l=[]
        mid=""
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in freq:
                l.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                mid = ch
        l="".join(l)
        r=l[::-1]
        return l+mid+r

        