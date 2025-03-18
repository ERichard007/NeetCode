#include <vector>
#include <map>
#include <queue>
#include <iostream>
using namespace std;

class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            map<int, int> dict;
            for (const int& num : nums){
                dict[num]++;
            }

            priority_queue<pair<int, int>> maxHeap;
            for (const auto& pair : dict){
                maxHeap.push(make_pair(pair.second, pair.first));
            }

            vector<int> solutionVector;
            while (k != 0)
            {
                solutionVector.push_back(maxHeap.top().second);
                maxHeap.pop();
                k--;
            }
            
            return solutionVector;
        }
    };

int main() {
    vector<int> nums = {1,2,2,3,3,3};
    int k = 2;

    Solution mySolution;
    vector<int> solution = mySolution.topKFrequent(nums, k);
    
    for (const int& num : solution){
        cout << num << " ";
    }

    return -1;
}