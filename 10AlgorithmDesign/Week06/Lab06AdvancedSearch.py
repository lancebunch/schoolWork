# 1. Name:
#      Lance Bunch
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program prompts for a file and word to search for then performs
#      an advanced search to determine if the word is in the file.
# 4. Algorithmic Efficiency
#      I believe that the algorithmic efficiency of this proram equates to 
#      O(log n). This is because at first the small files are almost equivalent
#      to the run time of the program, but as the input sizes drastically increase, the 
#      run time is barely effected.
# 5. What was the hardest part? Be as specific as possible.
#      This assignment went very smoothly. Nothing was quite complicated. I got stuck on
#      the len(data) for a moment as list data structures in python don't have a .size()
#      method mixed with them. Besides that I tried to follow smooth coding procedures
#      which manifest itself 10 fold. I spent almost as much time on the comments
#      as I did on the actual code. I attribute a big part of this to the psuedocode
#      that was developed last week.
# 6. How long did it take for you to complete the assignment?
#      In total this took me about 3.5 Hrs

import json

# This function is passed the name of a file in string format and
# attempts to open it. If successful the file is stored, converted
# to JSON, and converted to a list to prepare to search it.
def handle_file(filename):

    # Attempt to open the file
    try:
        file = open(filename)
        data_text = file.read()
        file.close()
    # If it fails, tell the user and quit the program
    except:
        print('Unable to open file ' + filename + '.')
        quit()

    # Convert the data_text to JSON format
    data_JSON = json.loads(data_text)

    # Assign the JSON data to a list
    data = data_JSON['array']

    # return the list of data
    return data

# This function finishes off the program by telling the user whether
# the word they want to find is in the file they specified or not.
def was_found(found, name, filename):
    if found:
        print('We found ' + name + ' in ' + filename + '.')
    else:
        print('We did not find ' + name + ' in ' + filename + '.')
    return

# My advnaced search function that grabs the name of the file and
# makes sure the file is valid. It then prompts the user for an word
# to search for and performs the advanced search algorithm to compute
# if the word is in the file. Following that it informs the user whether
# the word exists or not. Finally, it displays the efficiency metric 
# for the algorithm for me to determine how efficient my algorithm is.
def advanced_search():
    # Get the name of the file
    filename = input('What is the name of the file? ')

    # Decide if the name of the file is valid
    data = handle_file(filename)

    # Prompt for the name we are looking for
    name = input('What name are we looking for? ')

    # Setting advanced search variables
    i_first = 0
    i_last = len(data) - 1
    found = False

    # Efficiency Counter
    count = 0

    # While the start index is less than or equal the the end index
    while (i_first <= i_last) and not found:
        # i_middle is cast to an int to ensure there is no decimal for index references
        # This is also performed each time to revaulate where the middle of the list is
        i_middle = int((i_first + i_last) / 2)
        # If the middle of the list is alphabetically before the name we are searching for
        if data[i_middle] < name:
            # Move the beginning index up to the middle
            i_first = i_middle + 1
        # If the middle of the list is alphabetically after the name we are searching for
        elif data[i_middle] > name:
            # Move the ending index up to the middle
            i_last = i_middle - 1
        else:
            # Otherwise we found the word we are looking for
            found = True
        count += 1

    was_found(found, name, filename)

    # Printing my instrumentation to evaluate the efficiency of my algorithm
    print('n = ' + str(len(data)) + ', c = ' + str(count))

# For convenience, this is in a while loop to most easily run through the test cases
while True:
    advanced_search()
    print('\n\n\n')