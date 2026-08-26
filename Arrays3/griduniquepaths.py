class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        
        def pathCount(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            up = pathCount(i-1,j)
            down = pathCount(i,j-1)
            dp[i][j] = up + down
            return dp[i][j]

        return pathCount(m-1,n-1)
        