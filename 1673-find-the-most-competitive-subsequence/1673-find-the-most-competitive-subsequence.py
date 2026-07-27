class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s=[]
        n=len(nums)
        for i in range(n):
            while s and s[-1] > nums[i] and len(s) - 1 + (n - i) >= k:
                s.pop()
            s.append(nums[i])
        return s[:k]    

        