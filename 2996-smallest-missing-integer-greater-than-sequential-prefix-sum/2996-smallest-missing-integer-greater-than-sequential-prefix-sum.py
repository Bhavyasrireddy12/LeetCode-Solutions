class Solution:
    def missingInteger(self, nums: List[int]) -> int:
            sum=nums[0]
            i=1
            while i < len(nums) and nums[i]==nums[i-1]+1:
                sum+=nums[i]
                i+=1
            ans=sum
            while ans in nums:
                ans+=1
            return ans        



        