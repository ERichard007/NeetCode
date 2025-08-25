#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            vector<int> newList = {}, prefix = {}, postfix = {};
            
            int product = 1;
            for (const int& num : nums){
                product *= num;
                prefix.push_back(product);
            }

            product = 1;
            for (auto it = nums.rbegin(); it != nums.rend(); it++){
                product *= *it;
                postfix.push_back(product);
            }

            reverse(postfix.begin(), postfix.end());            
            
            for (int i = 0; i < nums.size(); i++){
                int number  = nums[i], prefixIndex = i-1, postfixIndex = i+1;
                int product = 1;

                if (prefixIndex >= 0){
                    product = prefix[prefixIndex];
                }

                if (postfixIndex <= nums.size()-1){
                    product *= postfix[postfixIndex];
                } 

                newList.push_back(product);
            }

            return newList;
        }
    };

int main(){
    Solution mySolution;
    vector<int> nums = {1,2,3,4};

    vector<int> newList = mySolution.productExceptSelf(nums);
    for (const int& n : newList){
        cout << n << endl;
    }

    return -1;
}