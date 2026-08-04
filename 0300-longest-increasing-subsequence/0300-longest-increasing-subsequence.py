from bisect import bisect_left
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            temp=[]
            for x in nums:
                pos=bisect_left(temp,x)
                if pos==len(temp):
                    temp.append(x)
                else:
                    temp[pos]=x
            return len(temp)            
        