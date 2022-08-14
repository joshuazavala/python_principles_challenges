# Function for finding the middle letter in a string and returning it
def mid (word):
    if len (word) % 2 == 0:
        return ""
    else:
        middle_number = len (word) // 2
        return word [middle_number]

# User input
user_word = input ("Type: ")

# Calling the function with user input
print (mid (user_word))
