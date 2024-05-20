#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAX_ADDITIVE = 4;
const int MAX_SUBTRACTIVE = 1;

string roman = "MDCLXVI";
int decimal [7] = {1000, 500, 100, 50, 10, 5, 1};

int findLetterIndex(char letter){
    int size = roman.size();
    for(int i = 0; i < size; i++){
        if(roman[i] == letter){
            return i;
        }
    }
    return -1;
}

int getNumDigitsDifference(char A, char B){
    int numA = getNumDigits(A);
    int numB = getNumDigits(B);
    return numB-numA;
}

int getNumDigits(char letter){
    int index = findLetterIndex(letter);
    if(index != -1){
        int num = decimal[index];
        int n = 1;
        while(num >= 10){
            n += 1;
            num /= 10;
        }
        return n;
    } else {
        throw std::invalid_argument("letter not found");
    }
}

int calculate(string in){
    int output = 0;

    while(in.size() > 0){
        
    }
    for(char& c : in){
        cout << getNumDigits(c);
    }
    return "hi";
}

int main(){
    string user_input = "none";

    while(user_input == "none"){
        cout << "Enter numeral or Q: ";
        cin >> user_input;

        if(user_input != "Q"){
            try{
                cout << user_input << " = " << calculate(user_input) << endl;
            } catch(...){
                cout << "Invalid" << endl;
            }
            user_input = "none";
        }
    }

    return 0;
}