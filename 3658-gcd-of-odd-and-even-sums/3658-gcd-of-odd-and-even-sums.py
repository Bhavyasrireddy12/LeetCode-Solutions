from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum=0
        evensum=0
        for i in range(1,n+1):
               evensum+=2*i
               oddsum+=2*i-1
        return gcd(oddsum,evensum)    
        
        