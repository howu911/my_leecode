'''
1 确定递归参数
    全局：
        result  [[]]
        path    单次遍历路径
    
    sum   当前路径和
    startIndex  起始遍历下标
    n   目标值
2 终止条件
    len(path) == k
        path和==n
3 单层遍历

'''

class Solution:
    def __init__(self):
            self.result = []
            self.path = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracing(startIndex, target_sum, sum, k):
            if len(self.path) == k:
                if target_sum == sum:
                    self.result.append(self.path[:])
                return
            
            for i in range(startIndex, 10):
                sum += i
                self.path.append(i)
                backtracing(i + 1, target_sum, sum, k)
                sum -= i
                self.path.pop()

        self.result.clear()
        self.path.clear()
        backtracing(1, n, 0, k)
        return self.result
