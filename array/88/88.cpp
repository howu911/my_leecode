/*
 * @Description: 88 合并两个有序数组
 * @Version: 1.0
 * @Autor: laijiatao
 * @Date: 2021-07-28 21:46:51
 * @LastEditors: laijiatao
 * @LastEditTime: 2021-07-29 22:26:13
 */

/**
 * @description: 
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for(int i= 0; i < nums2.size(); i++) {
            nums1[m+i] = nums2[i];
        }

        sort(nums1.begin(), nums1.end());
    }
};
