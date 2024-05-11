'''
1 确定dp数组以及下标含义
dp[i][j] 到达(i,j)有多少条不同的路径
2 确定递推公式
dp[i][j]来源与dp[i-1][j],dp[i][j-1]
3 dp数组初始化
初始化边界值
4 确定遍历顺序
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# 优化存储
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]  # 一行相当于上层的数据在当前层消费
        
        return dp[n-1]