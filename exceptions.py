# If the user inputs an actual number (like 5), we get the "happy path" and see the result of the addition
# If they enter a string (like "twenty"), we get the ValueError

print("A")
user_input = input("please give me a number:")
print(user_input)
try:
    result = 5 + int(user_input)
    print("That addition succeeded, and the result is", result)
except ValueError:
    print("The thing you entered is not a number.")
except TypeError:
    print("D")
else:
    print("E")
print("F")