'''
����һ��δ��������������飬�ҵ���� ���������������У������ظ����еĳ��ȡ�

���������������� �����������±� l �� r��l < r��ȷ�����������ÿ�� l <= i < r������ nums[i] < nums[i + 1] ����ô������ [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] �����������������С�

1 dp�����Լ��±�ĺ���
dp[i] ��nums[i]Ϊ��β�������������
2 ���ƹ�ʽ
if nums[i] > nums[i-1]:
    dp[i] = max(dp[i], dp[i-1] + 1)

3 dp�����ʼ��
���е������ʼ����Ϊ1
4 ����˳��
��ǰ����
5 ��ӡdp����
'''

class Solution:
    def findLengthOfLCIS(self, nums):
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i], dp[i-1] + 1)
        print(dp)
        return max(dp)
    

if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([2,2,2,2,2]))
