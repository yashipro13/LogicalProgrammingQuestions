#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool isPangram(string string1){
    int i = 97;
    char c;
    vector<char> all_letters;
    while (i <= 122){
        c = i;
        all_letters.push_back(c);
        i++;
    }
    vector<char> char_found;
    int count = 0;
    transform(string1.begin(), string1.end(), string1.begin(), ::tolower);
    i = 0;
    while (i < string1.length()){
        if (find(char_found.begin(), char_found.end(), string1[i]) == char_found.end() and find(all_letters.begin(), all_letters.end(), string1[i]) != all_letters.end()){
            char_found.push_back(string1[i]);
            count++;
        }
        i++;
    }
    return count == 26;
}
int main(){
    cout << isPangram("Pack my box with five dozen liquor jugs.");
    return 0;
}
