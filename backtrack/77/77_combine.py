class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []
        def backtracing(n, k, startIndex):
            if len(path) == k:
                result.append(path[:])  # 这里不能直接append path，path相当于是个地址
                return
            
            for i in range(startIndex, n-(k-len(path))+1+1):
                path.append(i)
                backtracing(n, k, i+1)
                path.pop()
        backtracing(n, k, 1)
        return result