from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        count=0
        for num,cnt in freq.items():
            if cnt > len(nums)//2:
                return num
       
            
        