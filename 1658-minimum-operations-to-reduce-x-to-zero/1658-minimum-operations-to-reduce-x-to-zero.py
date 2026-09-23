class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tot=sum(nums)
        target=tot-x
        if target<0:
            return -1
        left=0
        cursum=0
        maxlen=-1
        for right in range(len(nums)):
            cursum+=nums[right]
            while cursum>target:
                cursum-=nums[left]
                left+=1
            if cursum == target:
                maxlen=max(maxlen,right-left+1)
        if maxlen == -1:
            return -1
        return len(nums)-maxlen                

        