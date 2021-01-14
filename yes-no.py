# we want to be in the 'yes' situation whether the user enters Yes, YES, Y, y, or YeS...
# otherwise, we want to be in the 'no' situation.
# what if the answer is 'yoodle'?

while True:
    answer = input("hey, please enter Yes or No\n")
    # replace the user's answer with the lowercase version of it
    answer = answer.lower()

    if answer == "yes" or answer[0] == "y":
        print("yes situation")
    else:
        print("no situation")
    
    # extra line just for spacing
    print("")