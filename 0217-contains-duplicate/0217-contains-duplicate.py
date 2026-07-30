from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for i in range(len(nums)):
            if freq[nums[i]] > 1:
                return True
        return False        
            

    
        