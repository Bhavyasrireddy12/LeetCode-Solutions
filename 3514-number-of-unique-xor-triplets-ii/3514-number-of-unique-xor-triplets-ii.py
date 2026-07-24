class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        x=set(nums)
        x2 = set()
        for i in x:
            for j in x:
                x2.add(i ^ j)
        x3 = set()
        for k in x2:
            for i in x:
                x3.add(k ^ i)  
        return len(x3)               
                    
        