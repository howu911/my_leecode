'''
1 确定递归参数
    result []
    s    string

    digist_index    遍历数字的位数

2 终止条件
    digist_index == len(digits)

'''


class Solution:
    def __init__(self):
        self.result = []
        self.s = ''
        self.digist_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracing(digist_index, digits):
            if len(digits) == digist_index:
                self.result.append(self.s)
                return
            
            string = self.digist_map[digits[digist_index]]
            for c in string:
                self.s += c
                backtracing(digist_index + 1, digits)
                self.s = self.s[:-1]
        
        if not digits: return []
        self.result.clear()
        backtracing(0, digits)
        return self.result


        
