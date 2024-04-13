import math

dict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
    }

def LTN(l):
    return dict[l]

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def getNumDigits(letter):
    return GND(LTN(letter))

def getDifDigits(l1, l2):
    return abs(getNumDigits(l1)-getNumDigits(l2))

def GND(num):
    return int(math.log10(num))

def comparePlaces(n1, n2):
    d1, d2 = getNumDigits(n1), getNumDigits(n2)
    if d1 > d2:
        return 1
    elif d1 == d2:
        return 0
    else:
        return -1

def letterValid(letter):
    if letter in dict.keys():
        return True
    else:
        return False

def isSub(l1, l2):
    n1, n2 = getNumDigits(l1), getNumDigits(l2)
    if n1 <= n2:
        return True
    else:
        return False

def lastLetter(s):
    return s[len(s)-1]

def firstDigit(num):
    n = LTN(num)
    while n > 10:
        n /= 10
    return n

user_input = ""

while user_input == "":
    
    user_input = input("Enter numeral or Q: ")
    print(user_input)

    if user_input != "Q":
        last = 0
        output = ["","","",""]
        print(output)

        i = 0
        size = len(user_input)

        while i < size:
            letter = user_input[i]
            d = getNumDigits(letter)
            if i < size-1:
                next_letter = user_input[i+1]
                if isSub(letter, next_letter):
                    output[d-getDifDigits(letter, next_letter)] += (letter + next_letter)
                    i += 1
                else:
                    if letter not in output[d]:
                        output[d] += letter
                    elif firstDigit(letter) == 1:
                        if lastLetter(output[d]) == letter:
                            output[d] += letter

            elif i == size-1:
                if letter not in output[d]:
                    output[d] += letter
                elif firstDigit(letter) == 1:
                    if lastLetter(output[d]) == letter:
                        output[d] += letter
            i += 1
            print(output)

        
    
    user_input = ""