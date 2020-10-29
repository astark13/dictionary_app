import mysql.connector
from difflib import get_close_matches

# Connection to the Mysql DB using the mysql.connector module
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"    
)

cursor = con.cursor()
my_list = []
word = input("Type the word you are searching for:")

# This function queries the database for a word matching the string typed by the user
def search(word):                                  
    cursor.execute("SELECT * FROM Dictionary WHERE EXPRESSION = '%s'" %word)
    results = cursor.fetchall()               #type list
    return results

# The output of the 'search' function is saved in the 'content' variable
content = search(word)

# If no mathcing word was found by the previous function, 
# the following block provides some close matches for the string typed by the user 
query_expression_column = cursor.execute("SELECT Expression FROM Dictionary")
raw_expression_column = cursor.fetchall()

for result in raw_expression_column:
    # Checks the length of the output of the 'get_close_matches' function;
    # if the lengnth is greater than zero it means matches were found
    if len(get_close_matches(word, result)) > 0 :
        all_matches = get_close_matches(word, result, n=3, cutoff=0.8)
        # Appends to 'my_list' all matches(those that have the lenght greater than zero)
        for match in all_matches:
            if len(match) > 0:
               my_list.append(match)

# Removes duplicates from list
my_list = list(dict.fromkeys(my_list))        

if len(content) > 0 :
    for result in content:
        # Prints the second element of the list, in this case the definition of the searched word
        # The first element would be 'result[0]' 
        print(result[1])
elif len(my_list) > 0: 
    # After an input that has no match you are prompted with possible options,
    # and have the opportunity to retype the word you are searching for
    print("Did you mean one of the following words instead? \n\r")
    for item in my_list:
        print('- '+(item))
    print ("Please select one of them if it matches your search!")
    word = input("Retype the word you are searching for:")
    content = search(word)
    if len(content) > 0 :
        for result in content:
            print(result[1])
    # If you type for a second time a word that isn't present among the offerd options
    # you'll be prompted with a 'No results found!' message
    else:
        print("No results found!")
else:
    print("No results found!")                