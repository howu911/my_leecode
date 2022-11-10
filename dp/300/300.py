'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

1 dp数组以及下标的含义
dp[i] 以nums[i]为结尾的最长子序列
2 递推公式
存在nums[j] < nums[i]的情况:
dp[i] = max(dp[i], dp[j] + 1)

3 dp数组初始化
所有的数组初始化都为1
4 遍历顺序
从前往后
5 打印dp数组
'''

def lengthOfLIS1(nums):
    re = 1
    for i in range(len(nums)):
        all_max = nums[i]
        pre_max = nums[i]
        length = 1
        for j in range(i+1, len(nums)):
            if nums[j] > pre_max:
                if nums[j] < all_max:
                    length += 1
                    pre_max = nums[j]
                else:
                    all_max = nums[j]
                    length += 1
        re = max(re, length)
    return re

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(dp)

    return max(dp)


if __name__ == '__main__':
    print(lengthOfLIS([0,1,0,3,2,3]))

