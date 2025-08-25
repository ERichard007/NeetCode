#include <string>
#include <iostream>
using namespace std;

class Solution{
    public:
        bool isPalindrome(string s) {  /*O(n) space and time*/
            string compressed;
            for (const char& c : s){
                if (isdigit(c) || (static_cast<int>(tolower(c)) <= 122 && static_cast<int>(tolower(c)) >= 97)){
                    if (isalnum(c)){
                        compressed.push_back(tolower(c));
                    }
                }
            }

            int left = 0, right = compressed.length()-1;
            while (left < right){
                cout << compressed[left] << " and " << compressed[right] << endl;
                if (compressed[left] == compressed[right]){
                    left++;
                    right--;
                }else{
                    return false;
                }
            }

            return true;
    }
        bool betterIsPalindrome(string s){ /*O(n) time, O(1) space*/
            int l = 0, r = s.length()-1;
            while (l < r)
            {
                while (!isalnum(s[l]) && l < r){
                    l++;
                }

                while (!isalnum(s[r]) && l < r){
                    r--;
                }

                if(tolower(s[l]) == tolower(s[r])){
                    l++;
                    r--;
                }else{
                    return false;
                }
            }

            return true;
        }
};


int main(){
    string s = "Was it a car or a cat I saw?";
    Solution mySolution;

    cout << mySolution.isPalindrome(s) << endl;
    cout << mySolution.betterIsPalindrome(s) << endl;

    return 0;
}