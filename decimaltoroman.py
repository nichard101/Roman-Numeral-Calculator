import math

dict = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
    }

def firstDigit(num):
    n = LTN(num)
    while n > 10:
        n /= 10
    return n

def LTN(l):
    return dict[l]

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def getNumDigits(letter):
    return GND(LTN(letter))

def GND(num):
    return int(math.log10(num))

def getDifDigits(l1, l2):
    return abs(getNumDigits(l1)-getNumDigits(l2))

def getPow(num, p):
    i = 0
    while i < p:
        num *= num
    return num

def stringToList(string):
    list = []
    for letter in string:
        list.append(letter)
    return list

user_input = ""

while user_input == "":
    user_input = input("Enter integer: ")
    input_list = stringToList(user_input)
    for d in range(len(input_list)):
        input_list[d] = int(input_list[d])
    
    print(input_list)

    output = ""

    int_input = int(user_input)

    for d in dict.keys():
        while int_input >= d:
            int_input -= d
            output += dict[d]

    print(output)
