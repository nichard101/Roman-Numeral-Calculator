dict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

user_input = ""

while user_input == "":
    
    user_input = input("Enter numeral or Q: ")
    
    if user_input != "Q":
        l = 0
        n = 0
        while l < len(user_input):
            if l < len(user_input) - 1:
                if dict[user_input[l]] >= dict[user_input[l+1]]:
                    n += dict[user_input[l]]
                else:
                    n -= dict[user_input[l]]
            else:
                n += dict[user_input[l]]
            l += 1
        
        print("{} = {}".format(user_input, n))
        user_input = ""