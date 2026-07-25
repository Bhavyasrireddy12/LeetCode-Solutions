class Solution:
    def maxProduct(self, n: int) -> int:
            m1=0
            m2=0
            while n>0:
                c=n%10
                if c > m1:
                    m2=m1
                    m1=c
                elif c > m2:
                    m2=c
                n //= 10
            return m1*m2            

       
        