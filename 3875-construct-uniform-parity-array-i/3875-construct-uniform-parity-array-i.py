class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                print("Even:", nums1[i])
            else:
                print("Odd:", nums1[i])
        return True            

        