class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index = len(g) - 1
        s_index = len(s) - 1
        count = 0
        while s_index >= 0:
            if g_index < 0:
                break
            if g_index >= 0 and s[s_index] >= g[g_index]:
                count += 1
                s_index -= 1
            g_index -= 1
        
        return count