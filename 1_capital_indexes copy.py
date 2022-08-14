# Function for finding CAPITAL letters in a string and returning the index
def capital_indexes (text):
    return_list = []
    for i in range (0, len (text)):
        if text [i] == text [i].upper ():
            return_list.append (i)
        else:
            continue
    return return_list

# User input
user_input = input ("Type: ")

# Output of the index list
print (capital_indexes (user_input))
