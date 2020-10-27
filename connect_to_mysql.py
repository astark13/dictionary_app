import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"    
)

word = input("Type the word you are searching for:")

#def search(word):
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE EXPRESSION = '%s'" %word)
results = cursor.fetchall()

#search(word)

query_expression_column = cursor.execute("SELECT Expression FROM Dictionary")
raw_expression_column = cursor.fetchall()

my_list = []

for result in raw_expression_column:
    if len(get_close_matches(word, result)) > 0 :
        all_matches = get_close_matches(word, result, n=3, cutoff=0.8)
        for match in all_matches:
            if len(match) > 0:
               my_list.append(match)

my_list = list(dict.fromkeys(my_list))        #remove duplicates from list
#print(my_list)
                

if results:
    for result in results:
        print(result[1])
elif len(my_list) != 0: 
    print("Did you mean one of the following words instead? \n\r %s \n\r Please select one of them if it matches your search!" %my_list)
else:
    print("No results found!")
