# 1. Name: 
#    Lance Bunch
# 2. Assignment Name: 
#    Lab 02: Authentication
# 3. Assignment Description:
#    This lab showcases authenticating a user with a name
#    and password index match based off a JSON object. This
#    object contains the usernames and passwords.
# 4. What was the hardest part? Be as specific as possible.
#    One of the trickiest parts that I couldn't figure out is why
#    my logic in Python wouldn't allow me to check the indexes.
#    I had a bug in using (list_username.index(username)) and 
#    (list_password.index(password)) where even though the indexes
#    matched it wouldn't authenticate it. I'm still not sure as to 
#    why it didn't work the way I wanted it to. That resulted in me
#    iterating through the lists to see if the index matched along
#    with the usernames and passwords themselves. It shouldn't
#    have been as hard as it was.
# 5. How long did it take for you to complete the assignment?
#    5 Hours

import json

# Try to open the file
try:

    # Read the data from the file into a single string
    f = open('Lab02.json')

    # Convert the string into a JSON object (Python Dictionary) 
    data = json.load(f)

    # Covert username and password components of JSON object into two lists
    list_username = data["username"]
    list_password = data["password"]

    # Prompt the user for a username and password
    username = input('Username: ')
    password = input('Password: ')

    # Iterate through the length of the lists
    for i in range(len(list_username)):
        # If the indecies and text match in both lists
        if (list_username[i] == username) and (list_password[i] == password):
            # They are authenticated and the program is done.
            print('You are authenticated!')
            quit()

    # If we looped through everything and couldn't find a match
    print('You are not authorized to use the system.')

# If the file can't be found let them know
except:
    quit()
