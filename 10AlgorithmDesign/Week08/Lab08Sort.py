# 1. Name:
#      Lance Bunch
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program takes a file and sorts it from smallest value to greatest
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was the FOR loop displaying the list. I kept trying
#      to index the specific element in the array to display but I learned that by doing
#      'For i in [list],' using 'i' is an index to that element in the list. Everything else
#      Went very smoothly.
# 5. How long did it take for you to complete the assignment?
#      2 Hours

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
    # If there isn't any data in a list that was loaded then let the user know
    assert (data_JSON['array']), 'No data in List'
    data = data_JSON['array']

    # return the list of data
    return data


def slow_sort():
    # Get the name of the file
    filename = input('What is the name of the file? ')

    # If this is thrown make a loop that won't exit until the correct input is given
    assert (str(filename)), 'Name of file must be a string format'

    # Decide if the name of the file is valid
    data = handle_file(filename)

    # This loop is our pivot, it separates the unsorted list from the 
    # sorted list
    for i in range (0, (len(data) - 1)):
        # If this assert is thrown make sure the for loop is completed correctly.
        assert (i > 0), 'Error reading "i" index'
        i_pivot = i
        # This loop is our comparator. We compare every element in the list
        # until we find the element with the smallest value
        for j in range ((i + 1), len(data)):
            if data[j] < data[i_pivot]:
                i_pivot = j
        if i_pivot is not i:
            data[i], data[i_pivot] = data[i_pivot], data[i]

    print('The values in languages.json are:')
    for i in data:
        print('\t' + i)

while True:
    slow_sort()
    print('\n\n\n')