#include <vector>
#include <string>
#include <map>
#include <iostream>
using namespace std;

class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            map<vector<int>, vector<string>> dict;

            for (const string& s : strs){
                vector<int> key(26);
                for (const char& c : s){
                    key[static_cast<int>(c) - static_cast<int>('a')] += 1;
                }
                dict[key].push_back(s);
            }

            vector<vector<string>> solution;
            for (const auto& s : dict){
                solution.push_back(s.second);
            }

            return solution;
        }
    };
    
int main(){
    vector<string> input = {"act","pots","tops","cat","stop","hat"};
    Solution mySolution;
    
    vector<vector<string>> theSolution = mySolution.groupAnagrams(input);
    cout << "[";
    for (vector<string>& list : theSolution){
        cout << "[";
        for (string& str : list){
            if (str != list.back()){
                cout << str << ",";
            }else{
                cout << str;
            }
        }
        cout << "]";
    }
    cout << "]";

    return -1;
}