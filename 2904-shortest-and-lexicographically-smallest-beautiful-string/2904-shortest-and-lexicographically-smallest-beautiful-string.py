class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        ones=0
        minlen=float('inf')
        ans=""
        for right in range(len(s)):
            if s[right]=='1':
                ones+=1
            while ones>k:
                if s[left] == '1':
                    ones-=1
                left+=1
            while ones==k and s[left]=='0':
                left+=1
            if ones==k:
                curr=s[left:right+1] 
                currlen=len(curr)
                if currlen < minlen:
                    minlen = currlen
                    ans=curr
                elif currlen == minlen and curr<ans:
                    ans=curr
        return ans                              

        