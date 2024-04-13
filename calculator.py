dict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

def validate(input):
    r = 0
    l = 0

    # Count runs and run lengths of letters
    # Invalid if any run exceeds 3
    # If run of higher letter follows run of lower letter, invalid if run exceeds 1

    return True

def convert(input):
    l = 0
    n = 0
    while l < len(user_input):
        if l < len(user_input) - 1: # Check all digits which have a following digit
            if dict[user_input[l]] >= dict[user_input[l+1]]:
                n += dict[user_input[l]] # If next digit is lower, add value
            else:
                n -= dict[user_input[l]] # If next digit is higher, take value
        else:
            n += dict[user_input[l]] # Add value of final digit
        l += 1
    return n
    
while user_input == "":
    
    user_input = input("Enter numeral or Q: ")

    if user_input != "Q" and validate(user_input):
        print("{} = {}".format(user_input, convert(user_input)))
        user_input = ""