import json
from difflib import get_close_matches

# Import data from json format into a variable, as a dictionary
data = json.load(open("data.json"))
word = ((input("Enter the word you are loking for:")).lower())
capital = word.title()

# This function takes a word as input and compares it with the keys from the dictionary
def search(word):
    # If the word can be found in the dictionary keys, the value corresponding to it will be returned
    if word in data.keys():
        return data[word]
    # If te word isn't found, it tries to find a match turning the first letter in a capital letter
    elif capital in data.keys():
        return data[capital]
    #  "get_close_matches" function/method looks for the "word" against the dictionary keys "data.keys"; if it finds smth (the lenght of the item is >0) it prints it out
    elif len(get_close_matches(word, data.keys())) > 0:
        print ("Did you mean %s instead? If 'yes' type 'y', else type 'n':" % get_close_matches(word, data.keys())[0])
        confirm = input()
        if (confirm) == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif (confirm) == 'n':   
            return "The word does not exist! Please double check it!"
        else:
            return "We didn't understand your entry!"
    else:
        return "The word does not exist! Please double check it!"

definitions = search(word)

if type(definitions) == list:
    for description in definitions:
        print (description)
else:
    print(definitions)


