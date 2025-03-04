#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            int sum = 0;
            for (int x = 0; x < nums.size(); ++x){
                for (int y = x + 1; y < nums.size(); ++y){
                    if (nums[x] + nums[y] == target) {vector<int> solution = {x,y}; return solution;}
                }
            }
        }
    };


int main(){
    vector<int> inputNums = {-1,-2,-3,-4,-5};
    int target = -8;
    Solution newSolution;
    
    vector<int> solved = newSolution.twoSum(inputNums, target);

    for (const int& num : solved){
        cout << num << " ";
    }
    cout << endl;

    return -1;
}