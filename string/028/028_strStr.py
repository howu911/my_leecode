class Solution:
    def getNextFast(self, s, next):
        next.append(0)
        index = 1
        now = 0
        
        while index < len(s):
            if s[index] == s[now]:
                index += 1
                now += 1
                next.append(now)
            elif now:
                now = next[now - 1]
            else:
                next.append(0)
                index += 1
        
    
    def getNext(self, s, nextIndex):
        for i in range(nextIndex, 0, -1):
            if s[0:i] == s[nextIndex-i+1:nextIndex+1]:
                return i
        return 0
    
    def strStr(self, haystack: str, needle: str) -> int:
        haystackIndex = 0
        needleIndex = 0
        next = []
        self.getNextFast(needle, next)
        
        while haystackIndex < len(haystack):
            if haystack[haystackIndex] == needle[needleIndex]:
                haystackIndex += 1
                needleIndex += 1
            elif needleIndex:
                needleIndex = next[needleIndex-1]
            else:
                haystackIndex += 1
            
            if needleIndex == len(needle):
                return haystackIndex - needleIndex
        
        return -1