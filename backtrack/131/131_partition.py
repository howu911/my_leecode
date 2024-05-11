class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def partition(self, s):
        self.result.clear()
        self.path.clear()
        self.backtracing(0, s)
        return self.result

    def backtracing(self, startIndex, s):
        if startIndex >= len(s):
            self.result.append(self.path[:])
            return
        
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s, startIndex, i):
                self.path.append(s[startIndex:i + 1])
                self.backtracing(i + 1, s)  # 判断剩下的子串
                self.path.pop()  # 回溯

    def isPalindrome(self, s, startIndex, endIndex):
        while startIndex < endIndex:
            if s[startIndex] != s[endIndex]:
                return False
            startIndex += 1
            endIndex -= 1

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.partition('aab'))