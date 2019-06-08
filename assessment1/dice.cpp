#include <iostream>
#include <math.h>
#include <string>
#include <random>
using namespace std;
string throwDice(int num) {
    int x;
    int c1 = 0;
    int c2 = 0;
    int c3 = 0;
    int c4 = 0;
    int c5 = 0;
    int c6 = 0;
    string st;
    int arr[10];
    for (int i =0; i < num; i++){
        x = rand()%6 + 1;
        if (x == 1)
        c1++;
        else if (x == 2)
        c2++;
        else if (x == 3)
        c3++;
        else if (x == 4)
        c4++;
        else if (x == 5)
        c5++;
        else if (x == 6)
        c6++;
    }
    st = "one " + to_string(c1) + " two " + to_string(c2) + " three " + to_string(c3) + " four " + to_string(c4) + " five " + to_string(c5) + " six " + to_string(c6);
    return st;
}
int main(){
    cout<< throwDice(10000);
    cout<<"\n Expected results \n";
    int c1 = 10000 / 6;
    int c2 = 10000 / 6;
    int c3 = 10000 / 6;
    int c4 = 10000 / 6;
    int c5 = 10000 / 6;
    int c6 = 10000 / 6;
    string st = "one " + to_string(c1) + " two " + to_string(c2) + " three " + to_string(c3) + " four " + to_string(c4) + " five " + to_string(c5) + " six " + to_string(c6);
    cout << st;

    return 0;
}