class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        original=arr[:]
        arr.sort()
        rank=1
        mp={}
        for i in arr:
            if i in mp:
                continue
            mp[i]=rank
            rank+=1 
        ans=[]
        for i in original:
            ans.append(mp[i])
        return ans           



        