import math

MAX_ADDITIVE = 3
MAX_SUBTRACTIVE = 1

last_letter = ""

roman = ["M", "D", "C", "L", "X", "V", "I"]
decimal = [1000, 500, 100, 50, 10, 5, 1]

def R2D(letter):
    """
    Converts Roman character to decimal integer
    """
    if letter == None:
        return 0
    else:
        return decimal[roman.index(letter)]

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def getNumDigits(letter):
    """
    Returns number of digits in integer
    """
    return len(str(R2D(letter)))

def getDigitsDifference(A, B):
    """
    Returns difference between number of digits for A and B\n
    eg A=10(2), B=1000(4), output=2   
    """
    da, db = getNumDigits(A), getNumDigits(B)
    return db-da

def getFirstDigit(letter):
    num = R2D(letter)
    while num >= 10:
        num /= 10
    return num

def isSubtraction(l1, l2):
    d1, d2 = R2D(l1), R2D(l2)
    if d1 < d2:
        return True
    return False

def lastLetter(s):
    return s[len(s)-1]

def validateSlice(A, B=None, C=None): # UP DOWN
    """
    A       A>B=C   A>B>C   A>C>B
    A+B     A=B>C   
    B-A     B>A=C   B>A>C
    A+B+C   A=B=C
    """
    da, db, dc = R2D(A), R2D(B), R2D(C)
    print("{} {} {}".format(da,db,dc))

    if da == dc:
        if getFirstDigit(A) == 5:
            raise Exception("Error: {} {} {}".format(A,B,C))
    
    if da > db:
        if da > dc:
            if dc > db:
                return 2
            elif db == dc:
                return 1
            else:
                return 4
        elif da == dc:
            return 5
        else:
            raise Exception("Error: {} {} {}".format(A,B,C))
    elif da < db:
        if da > dc:
            return 3
        else:
            raise Exception("Error: {} {} {}".format(A,B,C))
    elif da == db:
        if db == dc:
            return 0
        else:
            raise Exception("Error: {} {} {}".format(A,B,C))

def countLetters(input, letter):
    n = 0
    for d in input:
        if letter == d:
            n += 1
    return n

def validateLetterCount(input, A):
    if isEven(roman.index(A)):
        return countLetters(input, A) <= (MAX_ADDITIVE + MAX_SUBTRACTIVE)
    else:
        return countLetters(input, A) <= 1
    
def validateLetter(letter):
    if letter in roman:
        return True
    else:
        return False

def validateAllLetters(input):
    for letter in input:
        if letter not in roman:
            raise Exception("Letter {} not valid".format(letter))

def validateRuns(input):
    score_dict = {}
    run = 1
    prev_letter = ""
    for letter in input:
        if letter not in score_dict.keys():
            score_dict[letter] = 1
        else:
            score_dict[letter] += 1
        
        if letter == prev_letter:
            run += 1
        else:
            run = 1
                
        if run > MAX_ADDITIVE:
            raise Exception("Exceeds max run length for {}".format(letter))
        
        prev_letter = letter
        
def processInput(user_input):
    output = 0
    validateAllLetters(user_input)
    validateRuns(user_input)
    while len(user_input) > 0:
        a = user_input[0]
        b = None
        c = None
        if len(user_input) >= 2:
            b = user_input[1]
        if len(user_input) >= 3:
            c = user_input[2]

        n = validateSlice(a, b, c)
        if n == 0:
            output += R2D(a)
            output += R2D(b)
            output += R2D(c)
            user_input = user_input[3:]
        elif n == 1:
            output += R2D(a)
            user_input = user_input[1:]
        elif n == 2:
            output += R2D(a)
            user_input = user_input[1:]
        elif n == 3:
            output += R2D(b)
            output -= R2D(a)
            user_input = user_input[2:]
        elif n == 4:
            output += R2D(a)
            output += R2D(b)
            user_input = user_input[2:]
        elif n == 5:
            output += R2D(a)
            output -= R2D(b)
            user_input = user_input[2:]
        print(output)
    return output

user_input = ""

while user_input == "":
    user_input = input("Enter numeral or Q: ")
    #print(user_input)

    if user_input != "Q":
        try:
            print("{} = {}".format(user_input, processInput(user_input)))
        except Exception as err:
            print(err.args)

    user_input = ""