class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        n = len(num)
        for i in range(n):
            while s and k > 0 and s[-1] > num[i]:
                s.pop()
                k-=1
            s.append(num[i])    
        if k > 0:
            s=s[:-k]
        result = "".join(s)
        result = result.lstrip('0')
        if result == "":
            return "0" 
        return result       
        