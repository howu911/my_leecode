/*
 * @Description: 121 买卖股票的最佳时机
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-07-25 10:15:00
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-07-25 10:40:17
 */

/**
 * @description: 第一次做，超时
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() <= 1) {
            return 0;
        }

        int max = 0;
        int liRui = INT_MIN;
        for(int i = 0; i < prices.size(); i++) {
            for(int j = i + 1; j < prices.size(); j++) {
                liRui = prices[j] - prices[i];
                if(max < liRui) {
                    max = liRui;
                }
            }
        }

        return max;
    }
};

/**
 * @description: 双指针： https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/shi-yong-shuang-zhi-zhen-ke-jie-by-chi-h-xd9o/
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */

class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, right = 0;
        int idax = 0;
        while ( right != prices.length ){
            idax = Math.max(prices[right] - prices[left], idax);
            if ( prices[right] < prices[left] )left = right;
            right++;
        }return idax;
    }
}

/**
 * @description: 动态规划：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0] 

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]



