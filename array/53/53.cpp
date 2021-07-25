/*
 * @Description: 53 最大子序和
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-07-24 22:35:21
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-07-24 22:55:26
 */

/**
 * @description: 第一次 通过，但复杂度是o(n2)
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int max = nums[0];

        for (int i = 0; i < nums.size(); i++) {
            sum = nums[i];
            if(sum > max) {
                max = sum;
            }

            for(int j = i + 1; j < nums.size(); j++) {
                sum += nums[j];
                if(sum > max) {
                    max = sum;
                }
            }

            sum = 0;
        }

        return max;
    }
};
