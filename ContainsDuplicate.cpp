#include <vector>
#include <iostream>
#include <sstream>
#include <set>
using namespace std;

class Solution {
    public:
        bool hasDuplicate(vector<int>& nums) {
            set<int> mySet;
            for (const int& num : nums){
                mySet.insert(num);
            }

            for (const int& num : mySet){cout << "SET: " << num << endl;}
            for (const int& num : nums){cout << "NUMS: " << num << endl;}

            return (mySet.size() == nums.size());
        }
    };

int main(){
    Solution mySolution;
    vector<int> myArray;
    string line;
    cin >> line;
    stringstream ss(line);
    int num;
    while (ss >> num){
        myArray.push_back(num);
    }
    bool theSolution = mySolution.hasDuplicate(myArray);
    cout << (theSolution == 1 ? "True" : "False") << endl;

    return -1;
}