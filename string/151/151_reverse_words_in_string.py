from operator import ne


class Solution:
    # 去除多余空格
    def removeSpace(self, s):
        left, right = 0, len(s)-1
        while left < right and s[left] == ' ':
            left += 1
        while left < right and s[right] == ' ':
            right -= 1
        
        new_s = []
        while left <= right:
            if s[left] == ' ' and s[left + 1] == ' ':
                left += 1
                continue
            new_s.append(s[left])
            left += 1
        return new_s

    # 翻转字符串
    def reverseString(self, s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
            
    # 翻转单词
    def reverseWord(self, s):
        left, right = 0, 0
        n = len(s)
        while left < n:
            while right < n and s[right] != ' ':
                right += 1
            
            s[left:right] = self.reverseString(s[left:right])
            left = right+1
            right += 1
        return s

    def reverseWords(self, s: str) -> str:
        new_s = self.removeSpace(s)
        # new_s = self.reverseString(new_s) # 这里为什么要接收一次新的列表
        # new_s = self.reverseWord(new_s)
        self.reverseString(new_s)
        self.reverseWord(new_s)
        return ''.join(new_s)

if __name__ == '__main__':
    s = Solution()
    new_s = s.reverseWords('  hello  world!  ')
    print(new_s)