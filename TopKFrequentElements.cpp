#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            map<int, int> dict;
            for (const int& num : nums){
                dict[num]++;
            }
            sort(dict.begin(), dict.end(), compare);

            for (const auto& pair : dict){
                cout << pair.first << ":" << pair.second << " " << endl; 
            }
            return nums;
        }
    private:
        bool compare (pair<int,int> &a, pair<int,int> &b){
            return a.second < b.second;
        }
    };

int main() {
    vector<int> nums = {1};
    int k = 2;
    Solution mySolution;

    vector<int> solution = mySolution.topKFrequent(nums, k);
    
    for (const int& num : solution){
        cout << num << " ";
    }

    return -1;
}