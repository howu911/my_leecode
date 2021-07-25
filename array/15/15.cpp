//15 三数之和
/**
 * @description: 第一次做时，使用去重排序的方式，会导致缺少元素，
 * 不排序，又会重复
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        sort(nums.begin(), nums.end());
        int n = unique(nums.begin(), nums.end()) - nums.begin();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    if(nums[i] + nums[j] + nums[k] == 0) {
                        result.push_back({nums[i], nums[j], nums[k]});
                    }
                    
                }
            }
        }

        return result;
    }
};

/**
 * @description: 参考：https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
 * @param {*}
 * @return {*}
 * @author: laijiatao
 */
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        if(nums.size() < 3)
            return result;

        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if(nums[i] > 0)
                break;
            if(i > 0 && nums[i] == nums[i-1])  // 去除重复元素
                continue;
            
            int L = i + 1;
            int R = n - 1;

            while(L < R){
                if(nums[i] + nums[L] + nums[R] == 0) {
                    result.push_back({nums[i], nums[L], nums[R]});
                
                    while(L < R && nums[R] == nums[R-1])  R -= 1;  //去重
                    while(L < R && nums[L] == nums[L+1])  L += 1;
                    L += 1;
                    R -= 1;
                }
                else if(nums[i] + nums[L] + nums[R] > 0)
                    R -= 1;
                else {
                    L += 1;
                }
            }
        }

        return result;
    }
};
