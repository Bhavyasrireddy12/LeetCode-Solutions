class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left+right) // 2
            sqr=mid*mid
            if sqr==x:
                return mid
            if sqr < x:
                ans=mid
                left = mid+1
            else:
                right = mid-1  
        return ans                     