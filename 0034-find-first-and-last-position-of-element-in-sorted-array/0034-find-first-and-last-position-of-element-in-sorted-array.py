class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            if not nums:
                return[-1,-1]
            left = 0 
            right = len(nums) - 1    
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid   
            if nums[left] != target:
                return[-1,-1] 
            first = left 
            left = 0
            right = len(nums) - 1 
            while left < right:
                mid = left + (right - left + 1) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid

            last = left
            return[first,last]        
        