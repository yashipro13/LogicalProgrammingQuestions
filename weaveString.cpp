#include <iostream>
#include <string>
using namespace std;

string weaveString (string string1, string string2){
    int small = string1.length();
    string big_string = string2;
    string output_string = "";
    if (string2.length() < small){
        small = string2.length();
        big_string = string1;
    }
    for (int i = 0; i < small; i++){
        output_string = output_string + string1[i] + string2[i];
    }
    output_string = output_string + big_string.substr(small,big_string.length());
    return output_string;
}

int main(){
    cout<< weaveString("Yashi","Rocket");

    return 0;
}
