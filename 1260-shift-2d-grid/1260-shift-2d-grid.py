class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total=m*n
        k%=total
        ans = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            ans.append(row)
        for i in range(m):
            for j in range(n):
                index = i * n + j
                newindex = (index+ k) % total

                newr = newindex // n
                newc = newindex % n

                ans[newr][newc] = grid[i][j]
        return ans            
                            


                            