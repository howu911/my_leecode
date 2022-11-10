class Solution:
    def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]  # python交换数据
            left += 1
            right -= 1
        return text
    
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for index in range(0, len(s_list), 2 * k):
            if index + k > len(s_list):
                s_list[index:] = s_list[index:][::-1]
            else:
                s_list[index:index + k] = s_list[index:index + k][::-1]
        return ''.join(s_list)