class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])   # 按照数组的第一维度进行升级

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    s = Solution()
    print(s.merge(intervals))
