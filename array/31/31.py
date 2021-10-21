class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 列表中的元素个数为1时，
        if not nums or len(nums) == 1:
            return
        
        # 原列表与反转后的列表相同时，反转列表
        if nums == sorted(nums)[::-1]:
            nums[:] = nums[::-1]
            return

        # 找到第一个下降的元素
        i = len(nums) - 1
        while(i-1 > 0 and nums[i-1] >= nums[i]):   #少个等于号出错  [2,2,7,5,4,3,2,2,1]
            i -= 1
        i -= 1

        # 找到第一个比nums[i]大的数
        j = len(nums) - 1
        while(j >= i and nums[j] <= nums[i]):
            j -= 1
            if nums[j] > nums[i]:
                break
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return


        
        