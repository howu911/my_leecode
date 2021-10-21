class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # �б��е�Ԫ�ظ���Ϊ1ʱ��
        if not nums or len(nums) == 1:
            return
        
        # ԭ�б��뷴ת����б���ͬʱ����ת�б�
        if nums == sorted(nums)[::-1]:
            nums[:] = nums[::-1]
            return

        # �ҵ���һ���½���Ԫ��
        i = len(nums) - 1
        while(i-1 > 0 and nums[i-1] >= nums[i]):   #�ٸ����ںų���  [2,2,7,5,4,3,2,2,1]
            i -= 1
        i -= 1

        # �ҵ���һ����nums[i]�����
        j = len(nums) - 1
        while(j >= i and nums[j] <= nums[i]):
            j -= 1
            if nums[j] > nums[i]:
                break
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return


        
        