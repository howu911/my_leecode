'''
1 确认backtrace递归参数
start_index: 本轮循环起始位置
point_num:ip小数点的个数

2 递归终止条件
point_num：为3时表示ip已经分割为4段
for statrt_index in range(0, len(s)):
    if point_num == 3:
        判断ip最后一个字段是否有效

3 单层遍历
判断start_index到i之间的字段是否有效
有效的话，往字符串中添加.
递归
擦除添加的.

'''


class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result.clear()
        if len(s) > 12:
            return []

        def backtracing(start_index, point_num, s):
            if point_num == 3:
                if self.isIpVaild(start_index, len(s)-1, s):
                    self.result.append(s[:])
                return

            for i in range(start_index, len(s)-1):
                if self.isIpVaild(start_index, i, s):
                    s = s[:i+1] + '.' + s[i+1:]
                    backtracing(i+2, point_num+1, s)
                    s = s[:i+1] + s[i+2:]
                else:
                    break
        
        backtracing(0, 0, s)
        return self.result


    def isIpVaild(self, start_index, end_index, s):
        if s[start_index] == '0' and start_index != end_index:
            return False
        
        if not 0 <= int(s[start_index:end_index+1]) <= 255:
            return False

        return True
