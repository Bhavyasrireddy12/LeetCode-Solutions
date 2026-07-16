from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        prefixgcd=[]
        for i in nums:
            mx=max(mx,i)
            prefixgcd.append(gcd(i,mx))
        prefixgcd.sort()    
        left=0
        right=len(prefixgcd)-1
        ans=0
        while left<right:
            ans+=gcd(prefixgcd[left],prefixgcd[right])
            left+=1
            right-=1
        return ans    

        
         









        