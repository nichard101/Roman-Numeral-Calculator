#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAX_ADDITIVE = 3;
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

int getFirstDigit(char letter){
    int n = decimal[findLetterIndex(letter)];
    while(n >= 10){
        n /= 10;
    }
    return n;
}

bool isSameDigit(char a, char b){
    int one = getFirstDigit(a);
    int two = getFirstDigit(b);
    if(one==two){
        return true;
    } else {
        return false;
    }
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
        throw runtime_error("letter not found");
    }
}

int getNumDigitsDifference(char A, char B){
    int numA = getNumDigits(A);
    int numB = getNumDigits(B);
    return numB-numA;
}

int findOperation(char a, char b, char c){
    int da = decimal[findLetterIndex(a)];
    int db = decimal[findLetterIndex(b)];
    int dc = decimal[findLetterIndex(c)];

    if(da<dc){
        throw runtime_error("invalid order of ascension");
    }

    if(da==dc){
        if(getFirstDigit(a) == 5){
            throw runtime_error("two 5s of same kind");
        }
        if(db > da){
            throw runtime_error("incorrect ascension");
        }
        if(getNumDigitsDifference(a,b) > 1){
            throw runtime_error("incorrect descension");
        }
    }

    if(db>da){
        if(da==dc){
            if(getFirstDigit(a) == 5){
                throw runtime_error("two 5s of same kind");
            }
            if(getNumDigitsDifference(a,b) < -1){
                throw runtime_error("incorrect descension");
            }
        }
        if(getNumDigitsDifference(a,b) > 1){
            throw runtime_error("incorrect descension");
        }
        if(getNumDigitsDifference(a,b) == 1 && !isSameDigit(a,b)){
            throw runtime_error("incorrect descension");
        }
        return 1;
    }

    if(dc>db){
        if(getFirstDigit(b) != 1){
            throw runtime_error("wrong digit for subtraction");
        }
        if(getNumDigitsDifference(b,c) > 0){
            if(getNumDigitsDifference(b,c) > 1 || !isSameDigit(b,c)){
                throw runtime_error("incorrect order of ascension");
            }
        }
    }

    if(da>=db){
        if(da==db){
            if(getFirstDigit(a) == 5){
                throw runtime_error("two 5s of same kind");
            }
        }
        return 0;
    }
    return -1;
}

void validateLetters(string in){
    for(int i = 0; i < in.size(); i++){
        if(roman.find(in[i]) == string::npos){
            throw runtime_error("invalid character");
        }
    }
}

void validateRuns(string in){
    int run = 1;
    char prev_letter = ' ';
    for(int i = 0; i < in.size(); i++){
        char letter = in[i];
        if(letter == prev_letter){
            run += 1;
        } else {
            run = 1;
        }

        if(run > MAX_ADDITIVE){
            throw runtime_error("exceeds max run length");
        }

        prev_letter = letter;
    }
}

int calculate(string in){

    validateLetters(in);
    validateRuns(in);

    int output = 0;

    while(in.size() > 0){
        char a = in[0];
        char b = 0, c = 0;

        if(in.size() >= 2){
            b = in[1];
        }
        if(in.size() >= 3){
            c = in[2];
        }

        int n = findOperation(a,b,c);

        if(n==0){ // Addition
            output += decimal[findLetterIndex(a)];
            in = in.substr(1);
        } else if(n==1){ // Subtraction
            output -= decimal[findLetterIndex(a)];
            output += decimal[findLetterIndex(b)];
            in = in.substr(2);
        }

    }
    return output;
}

int main(){
    string user_input = "none";

    while(user_input == "none"){
        cout << "Enter numeral or Q: ";
        cin >> user_input;

        if(user_input != "Q"){
            try{
                int final_output = calculate(user_input);
                cout << user_input << " = " << final_output << endl;
            } catch(const runtime_error& err){
                cout << err.what() << endl;
            }
            user_input = "none";
        }
    }

    return 0;
}