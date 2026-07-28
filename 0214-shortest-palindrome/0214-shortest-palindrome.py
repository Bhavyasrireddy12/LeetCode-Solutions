class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev=s[::-1]
        temp = s +"#"+rev
        lps=[0] * len(temp)
        j=0
        for i in range(1,len(temp)):
            while j > 0 and temp[i]!=temp[j]:
                j=lps[j - 1]
            if temp[i] == temp[j]:
                j+=1
                lps[i]=j    
        pl=lps[-1]
        suffix=s[pl:]
        return suffix[::-1]+s