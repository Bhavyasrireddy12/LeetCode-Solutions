class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        current=0
        previous=0
        res=[]
        for i in range(numRows):
            current=[1] *(i+1)
            for j in range(1,i):
                current[j]=res[i-1][j-1]+res[i-1][j]
            res.append(current)
        return res        



        