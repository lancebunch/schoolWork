# 1. Name:
#      Lance Bunch
# 2. Assignment Name:
#      Lab 12: Prime Numbers
# 3. Assignment Description:
#      This program prompts the user for an integer, and finds all primes up to and
#      potentially including that specific number.
# 4. What was the hardest part? Be as specific as possible.
#      The loops determining prime numbers were tricky. At first I wanted to go through 
#      each number up to the sqr root of n to determine if it was a prime. This would 
#      have been extremely inefficient, though. Instead I found that keeping track of
#      multiples would be the easiest and most efficient way to determine prime numbers.
#      After that the hardest part was coming up with asserts again as there is only one
#      opportunity for input and that asserts covers the basis.
# 5. How long did it take for you to complete the assignment?
#      3 Hrs

# Grabbing the integer the user would like to see prime numbers to
n = int(input('This program will find all the prime numbers at or below N. Select that N: '))

# If this assert is thrown, add an indefinite loop until correct input is given
assert (n >= 0), 'Number must be a positive integer'
assert (n < 10000000), 'There is no point knowing primes greater than 10000000'

# Creating a boolean list to keep track of prime numbers
numbers = [True for i in range(n + 1)]

# p is our tracker. It starts at 2 as 2 is the first prime number
p = 2

# While the tracker is less than the square root of n...
while(p * p <= n):
        # If we have found a prime number...
        if(numbers[p] == True):
            # All of its multiples are NOT prime numbers
            for i in range (p * p, n + 1, p):
                numbers[i] = False
        p +=1

# Initializing our prime number list
primes = []

# For every number starting at 2 until our n...
for i in range(2, n + 1):
    # if the index is true that means it is a prime number...
    if numbers[i]:
        # so put it in our prime number list
        primes.append(i)

# Show the user all the primes up to/including their number
print('The prime numbers at or below ' + str(n) + ' are ' + str(primes))