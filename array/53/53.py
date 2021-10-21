'''
����һ���������� nums ���ҵ�һ���������͵����������飨���������ٰ���һ��Ԫ�أ������������͡�

1 dp�����Լ��±�ĺ���
dp[i] ��i��������[0,i]����������
2 ���ƹ�ʽ
��i����������Ϳ�dp[i-1]�Ƿ��num[i]������
if dp[i] < 0:
    dp[i] = num[i]
else:
    dp[i] = dp[i-1] + num[i]

���ϳ���һ�¿��Ա�Ϊ
dp[i] = max(dp[i-1] + num[i], num[i])

3 dp�����ʼ��
dp[0] = num[0]

4 ����˳��
��ǰ����
5 ��ӡdp����

'''
class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        print(dp)
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

