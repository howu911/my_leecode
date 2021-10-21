'''
1 dp数组以及下标的含义
dp[i] 第i项数字是第i-1项和i-2项之和
2 递推公式
F(n) = F(n - 1) + F(n - 2)
3 dp数组初始化
F(0) = 0，F(1) = 1
4 遍历顺序
从前往后
5 打印dp数组
'''

class Solution:
    def fib(self, n):
        dp = [0] * (n + 2)
        dp[0] = 0
        dp[1] = 1
        if n >= 0 and n < 2:
            return dp[n]
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.fib(3))
