# https://leetcode.cn/problems/repeated-substring-pattern/solution/by-code_python-vdfy/
# https://leetcode.cn/problems/repeated-substring-pattern/solution/by-tian-shen-bu-pa-i0gh/


class FindSubStr:
    def getNext(self, s):
        nextList = []
        nextList.append(0)
        left = 0
        right = 1
        
        while right < len(s):
            if s[left] == s[right]:
                nextList.append(left + 1)
                left += 1
                right += 1
            elif left:
                left = nextList[left - 1]
            else:
                nextList.append(0)
                right += 1
        
        return nextList
    
    def findStr(self, s, p):
        sIndex, pIndex = 0, 0
        next = self.getNext(p)
        
        while pIndex < len(p) and sIndex < len(s):
            if p[pIndex] == s[sIndex]:
                pIndex += 1
                sIndex += 1
            elif pIndex:
                pIndex = next[pIndex - 1]
            else:
                pIndex = 0
                sIndex += 1
        if pIndex == len(p):
            return sIndex - pIndex
        return -1

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_s = s + s
        method = FindSubStr()
        return method.findStr(new_s[1:-1], s) != -1
    
if __name__ == '__main__':
    s = FindSubStr()
    print(s.getNext('abcabcabc'))
    print(s.findStr('abaabaaabaabaa'[1:-1], 'abaabaa'))