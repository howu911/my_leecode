'''
718 最长重复子数组

给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

1 dp数组以及下标的含义
dp[i][j] 以nums1[i-1] nums2[j-1]为结尾的最长子数组长度
-1是为了遍历时缺少前一个值的初始化

2 递推公式
存在nums[j] < nums[i]的情况:
dp[i] = max(dp[i], dp[j] + 1)

3 dp数组初始化
所有的数组初始化都为1

4 遍历顺序
从前往后

5 打印dp数组
'''

class Solution:
    def findLength(self, nums1, nums2):
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        result = 0

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])

        return result

if __name__ == '__main__':
    sc = Solution()
    print(sc.findLength([1,0,0,0,1], [1,0,0,1,1]))
