#include <vector>
#include <map>
#include <queue>
#include <iostream>
using namespace std;

/*using bucket sort this time instead of max Heap!*/

class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            map<int, int> count;
            for (const int& num : nums){
                count[num]++;
            }

            vector<vector<int>> frequency(nums.size() + 1);
            for (const auto& pair : count){
                cout << pair.first << ":" << pair.second << endl;
                frequency[pair.second].push_back(pair.first);
            }

            vector<int> solutionVector;
            for (int x = frequency.size()-1; x >= 0 && k > 0; x--){
                for (const int& num : frequency.at(x)){
                    solutionVector.push_back(num);
                    k--;
                    if (k == 0){return solutionVector;}
                }
            }

            return solutionVector;
        }
    };

int main() {
    vector<int> nums = {1, 2, 3, 4, 5};
    int k = 3;

    Solution mySolution;
    vector<int> solution = mySolution.topKFrequent(nums, k);
    
    for (const int& num : solution){
        cout << num << " ";
    }

    return -1;
}