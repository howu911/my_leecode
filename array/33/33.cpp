/*
 * @Description: 33 搜索螺旋数组
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-08-08 10:05:50
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-08-08 15:50:45
 */

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0, end = nums.size() - 1;
        int mid = 0;

        while (start <= end) {
            mid = (start + end) / 2;
            if(target == nums[mid]) {
                return mid;
            }

            if(nums[start] <= nums[mid]) {  // 前半段有序，在前半段判断是否有target  注意=，当有两个元素，且目标值在第二个
                if(target >= nums[start] && target < nums[mid]) {
                    end = mid - 1;
                }
                else {
                    start = mid + 1;
                }
            }
            else {
                if(target > nums[mid] && target <= nums[end]) {
                    start = mid + 1;
                }
                else {
                    end = mid - 1;
                }
            }
            
        }
        return -1;
    }
};
