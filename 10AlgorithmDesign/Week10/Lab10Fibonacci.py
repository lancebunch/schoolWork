# 1. Name:
#      Lance Bunch
# 2. Assignment Name:
#      Lab 10: Fibonacci
# 3. Assignment Description:
#      This program is meant to prompt the user for a number and perform Fibonacci
#      math to see th value of the number in the Fibonacci sequence
# 4. What was the hardest part? Be as specific as possible.
#      This assignment was very easy. The hardest part was finding a valid 3rd 'assert' as the
#      program itself is quite straight forward. There is only 1 opportunity for input and the 
#      rest of the program is covered as far as buginess goes. 
# 5. How long did it take for you to complete the assignment?
#      1.5 HRS

while (True):
    fib_num = int(input('Which Fibonacci number would you like to see? '))

    # If either of these are thrown, make a loop that won't continue until an appropriate 
    # value is given.
    assert (fib_num >= 0), 'Number must be a positive integer.'
    assert (fib_num <= 100000), 'Integer value is too large.'

    # Initiating my values at the start of the Fibonacci sequence
    fib1 = 1
    fib2 = 1
    fib3 = 1

    # This FOR loop will add and keep track of each number in the Fibonacci 
    # sequence until we meet the desired Fibonacci number
    for i in range (1, fib_num):
        fib1 += fib2
        fib2 = fib3
        fib3 = fib1

    # Give the user what they asked for and print some newlines to start over again
    print('Fibonacci number ' + str(fib_num) + ' is ' + str(fib1))
    print('\n\n\n')