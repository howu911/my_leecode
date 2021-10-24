'''
给你一个字符串 s，找到 s 中最长的回文子串。

1 dp数组以及下标的含义
dp[i][j]表示区间i j间的数组是否是回文子串
2 递推公式
在确定递推公式时，就要分析如下几种情况。

整体上是两种，就是s[i]与s[j]相等，s[i]与s[j]不相等这两种。

当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。

当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况

情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
情况二：下标i 与 j相差为1，例如aa，也是文子串
情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

3 dp数组初始化
全部初始化为false
4 遍历顺序
首先从递推公式中可以看出，情况三是根据dp[i + 1][j - 1]是否为true，在对dp[i][j]进行赋值true的。
dp[i + 1][j - 1] 在 dp[i][j]的左下角
从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的
5 打印dp数组

中心拓展法：
class Solution {
public:
    int left = 0;
    int right = 0;
    int maxLength = 0;
    string longestPalindrome(string s) {
        int result = 0;
        for (int i = 0; i < s.size(); i++) {
            extend(s, i, i, s.size()); // 以i为中心
            extend(s, i, i + 1, s.size()); // 以i和i+1为中心
        }
        return s.substr(left, maxLength);
    }
    void extend(const string& s, int i, int j, int n) {
        while (i >= 0 && j < n && s[i] == s[j]) {
            if (j - i + 1 > maxLength) {
                left = i;
                right = j;
                maxLength = j - i + 1;
            }
            i--;
            j++;
        }
    }
};

作者：carlsun-2
链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/dai-ma-sui-xiang-lu-5-zui-chang-hui-wen-kgyl1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def longestPalindrome(self, s):
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        max_length, left, right = 0, 0, 0
        for i in range(len(s)-1, -1, -1):   # 从下往上
            for j in range(len(s)):     # 从左往右
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = 1
                
                if dp[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    left = i
                    right = j

        print(dp)
        return s[left:right+1]

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
