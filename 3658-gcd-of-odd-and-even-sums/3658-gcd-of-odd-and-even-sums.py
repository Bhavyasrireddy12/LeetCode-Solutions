class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum=0
        evensum=0
        for i in range(1,n):
            if i%2==0:
               evensum+=2*i
            else:
                oddsum+=2*i-1
            gcd(oddsum,evensum)    
        return n
        