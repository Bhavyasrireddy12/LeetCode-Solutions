from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq=Counter()
        for i in range(len(nums)-k+1):
            freq.update(set(nums[i:i+k]))
        for x in range(50,-1,-1):
            if freq[x]==1:
                return x
        return -1        

        