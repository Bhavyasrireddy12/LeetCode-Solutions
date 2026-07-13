class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        ans=[]
        minlen=len(str(low))
        maxlen=len(str(high))
        for length in range(minlen,maxlen+1):
            for i in range(10-length):
                num=int(s[i:i + length])
                if low<=num<=high:
                    ans.append(num)
        return ans