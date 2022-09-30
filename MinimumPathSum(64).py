class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid_c = [[0]*len(grid[0]) for i in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmp = 0
                if i-1 >= 0 and i - 1 < len(grid):
                    tmp = grid_c[i - 1][j]
                if j - 1 >= 0 and j - 1 < len(grid[0]):
                    tmp = grid_c[i][j - 1] if tmp == 0 else min(tmp,grid_c[i][j - 1])
                grid_c[i][j] += tmp + grid[i][j]
        
        return grid_c[len(grid) - 1][len(grid[0]) - 1]