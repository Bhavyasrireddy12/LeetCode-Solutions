class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        digitsum=sum(digits)
        prod=1
        for d in digits:
            prod *= d
        totsum=digitsum+prod
        return n % totsum==0    

        