#include <iostream>
#include <string>
using namespace std;

bool isAmbigous(string date_string){
    int start = 0;
    string fp = " ";
    while (date_string[start] != '/'){
        fp = fp + date_string[start];
        start = start + 1;
    } 
    start = start + 1;
    string sp=" ";
    while (date_string[start] != '/'){
        sp = sp + date_string[start];
        start = start + 1;
    }
    int f_part = stoi(fp);
    int s_part = stoi(sp);
    return ((f_part <= 12) and (s_part <= 12)); 

}

int main(){
    cout<< isAmbigous("20/03/1999");
    return 0;
}