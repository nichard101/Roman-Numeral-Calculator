MAX_ADDITIVE = 3
MAX_SUBTRACTIVE = 1

ROMAN = ["M", "D", "C", "L", "X", "V", "I"]
DECIMAL = [1000, 500, 100, 50, 10, 5, 1]

def R2D(letter):
    """
    Converts Roman character to decimal integer
    """
    if letter == None:
        return 0
    else:
        return DECIMAL[ROMAN.index(letter)]

def isEven(num):
    """
    Returns True if even, False if odd
    """
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
    """
    Returns first integer digit of input Roman numeral
    """
    num = R2D(letter)
    while num >= 10:
        num /= 10
    return num

def isSameDigit(letterA,letterB):
    """
    Returns True if the first digits match, False otherwise
    """
    return getFirstDigit(letterA) == getFirstDigit(letterB)

def findOperation(A, B=None, C=None): # UP DOWN
    """
    A       A>B=C   A>B>C   A>C>B
    A+B     A=B>C   
    B-A     B>A=C   B>A>C
    A+B+C   A=B=C
    """
    da, db, dc = R2D(A), R2D(B), R2D(C)
    dac, dab, dbc = getDigitsDifference(A,C), getDigitsDifference(A,B), getDigitsDifference(B,C)

    if da < dc:
        raise Exception("Error: Incorrect order of ascension (C) - {} {} [{}]".format(A,B,C))
    
    if da == dc:
        if getFirstDigit(A) == 5:
            raise Exception("Error: Two 5s of same kind - [{}] {} [{}]".format(A,B,C))
        if db > da:
            raise Exception("Error: Incorrect ascension (B) - {} [{}] {}".format(A,B,C))
        if dab < -1:
            raise Exception("Error: Incorrect descension (B) - {} [{}] {}".format(A,B,C))
    
    if db > da:
        if da == dc:
            if getFirstDigit(A) == 5:
                raise Exception("Error: Two 5s of same kind - [{}] {} [{}]".format(A,B,C))
            if dab < -1:
                raise Exception("Error: Incorrect descension (B) - {} [{}] {}".format(A,B,C))        
        if getDigitsDifference(A,B) >= 1:
            if getDigitsDifference(A,B) > 1 or (getDigitsDifference(A,B) == 1 and not isSameDigit(A, B)):
                raise Exception("Error: Incorrect ascension (B) - {} [{}] {}".format(A,B,C))
        return 1

    if dc > db:
        if getFirstDigit(B) != 1:   # Only 1s can come before higher digits
            raise Exception("Error: Wrong digit for subtraction - {}".format(B))
        if getDigitsDifference(B,C) > 0:
            if getDigitsDifference(B,C) > 1:
                raise Exception("Error: Incorrect order of ascension (B^C) - {} {}".format(A,B))
            elif not isSameDigit(B,C):
                raise Exception("Error: Wrong subtraction combination - {} {}".format(A,B))   
    if da >= db:
        return 0

def countLetters(input, letter):
    """
    Returns number of occurrences of input letter within input string
    """
    n = 0
    for d in input:
        if letter == d:
            n += 1
    return n

def validateAllLetters(input):
    """
    Checks if all letters in input string are valid Roman numerals
    """
    for letter in input:
        if letter not in ROMAN:
            raise Exception("Letter {} not valid".format(letter))

def validateRuns(input):
    """
    Checks that input string does not contain more than a set amount of the same character in succession
    """
    run = 1
    prev_letter = ""
    for letter in input:       
        if letter == prev_letter:
            run += 1
        else:
            run = 1
                
        if run > MAX_ADDITIVE:
            raise Exception("Exceeds max run length for {}".format(letter))
        
        prev_letter = letter
        
def processInput(user_input):
    """
    Takes string input and converts it to integer number output
    """

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

        n = findOperation(a, b, c)

        if n == 0:
            output += R2D(a)
            user_input = user_input[1:]

        elif n == 1:
            output -= R2D(a)
            output += R2D(b)
            user_input = user_input[2:]

    return output


#############################################################

user_input = ""

while user_input == "":
    user_input = input("Enter numeral or Q: ")
    if user_input != "Q":
        try:
            print("{} = {}".format(user_input, processInput(user_input)))
        except Exception as err:
            print(err.args)
    user_input = ""