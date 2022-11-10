class Solution:
    def replaceSpace(self, s: str) -> str:
        space_count = s.count(' ')
        s_list = list(s)
        s_list.extend([' '] * space_count * 2)
        
        left, right = len(s) - 1, len(s_list) - 1
        while left != right:
            if s_list[left] == ' ':
                s_list[right - 2:right+1] = ['%', '2','0'] # 左闭右开
                left -= 1
                right -= 3
            else:
                s_list[right] = s_list[left]
                left -= 1
                right -= 1
        return ''.join(s_list)