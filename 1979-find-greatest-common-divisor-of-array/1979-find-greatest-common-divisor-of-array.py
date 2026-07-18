class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largest = nums[0]
        smallest = nums[0]
        for x in nums:
            smallest=min(smallest,x)
            largest=max(largest,x)
        return gcd(smallest,largest)     


        