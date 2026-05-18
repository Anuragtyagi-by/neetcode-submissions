class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int length = nums.size();
        vector<int> returnArray = {};
        for (int i = 0;i<length;i++) {
            for (int j = i+1; j<length;j++) {
                if(nums[i] + nums[j] == target) {
                    returnArray = {i,j};
                    return returnArray;
                }
            }
        
        }
        return returnArray;
    }
};
