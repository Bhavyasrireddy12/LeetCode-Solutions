class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        minsuf=[0]*n
        minsuf[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            minsuf[i]=min(nums[i],minsuf[i+1])
        maxsf=nums[0]
        for i in range(n):
            maxsf=max(maxsf,nums[i])
            score=maxsf - minsuf[i]
            if score <= k:
                return i
        return -1        
        