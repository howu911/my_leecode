'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

1 dp数组以及下标的含义
dp[i] 前i天的的最大收益
2 递推公式
统计出前i天的最低价格，minPrice
dp[i] = max(dp[i-1], price[i]-minPrice)
3 dp数组初始化
minPrice = price[0]
dp[i] = 0
4 遍历顺序
从前往后
5 打印dp数组
'''

class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        dp = [0] * len(prices)
        minPrice = prices[0]

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i-1])
            dp[i] = max(dp[i-1], prices[i]-minPrice)
        
        print(dp)
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))

