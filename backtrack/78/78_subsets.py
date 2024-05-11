'''
参数：
    path 子集收集单次遍历结果
    result 收集所有结果
    startindex 单层搜索的起始地址 
终止条件：
    消耗完叶子节点，即startindex > 数组的长度
单层遍历

'''

class Solution:
    def __init__(self) -> None:
        self.path = []
        self.result = []

    def subsets(self, nums):
        def backtracking(startindex, nums):
            self.result.append(self.path[:])
            for index in range(startindex, len(nums)):
                self.path.append(nums[index])
                backtracking(index+1, nums)
                self.path.pop()
        
        self.result.clear()
        self.path.clear()
        backtracking(0, nums)
        return self.result

if __name__ == '__main__':
    s = Solution()
    s.subsets([1,2,3])
    print(s.result)

