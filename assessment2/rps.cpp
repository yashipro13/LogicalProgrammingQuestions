#include <iostream>
#include <string>
using namespace std;
int playRps(string c1, string c2){
    if (c1 == c2)
        return 0;
    else if ((c1 == "R" and c2 == "P") or (c1 == "S" and c2 == "R" ) and (c1 == "P" and c2 == "R"))
        return -1;
    else
        return 1;
}
string resultRps(string inp_string){
    int i = 0;
    int draw = 0;
    int win = 0;
    int loss = 0;

    while (i < inp_string.length()){
    
        if (playRps(to_string(inp_string[i]), to_string(inp_string[i+1])) == 0){
            draw += 1;
        }
        else if (playRps(to_string(inp_string[i]), to_string(inp_string[i+1])) == 1){
            win += 1;
        }
        else{
            loss += 1;
        }
        i = i + 3;
        }
        
        return "+ " + to_string(win) + "\t - " + to_string(loss) + "\t = " + to_string(draw);
    }
     
    int main(){
        cout << resultRps("RR,RP,RS,SS");
    }
