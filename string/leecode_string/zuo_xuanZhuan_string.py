class Solution:
    def reverseWord(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    def reverseLeftWords(self, s: str, n: int) -> str:
        new_s = list(s)
        self.reverseWord(new_s, 0, len(new_s)-1)
        self.reverseWord(new_s, 0, len(new_s)-n -1)
        self.reverseWord(new_s, len(new_s)-n, len(new_s)-1)
        return ''.join(new_s)
        
if __name__ == '__main__':
    s = Solution()
    new_s = s.reverseLeftWords('helloworld!', 3)
    print(new_s)