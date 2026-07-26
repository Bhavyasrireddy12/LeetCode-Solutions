class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        m1=m2=m3=float('-inf')
        min1=min2=float('inf')
        for c in nums:
            if c > m1:
                m3=m2
                m2=m1
                m1=c
            elif c > m2:
                m3 = m2
                m2=c
            elif c > m3:
                m3 = c    
            if c < min1:
                min2=min1
                min1=c
            elif c < min2:
                min2 = c    
        return max(m1*m2*m3,m1*min1*min2)        

        