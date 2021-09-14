# 1. Name:
#      Lance Bunch
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program calculates what it takes to build a Hotel on Penn Ave
# 4. What was the hardest part? Be as specific as possible.
#      If I were to deal with it I think the hardest part would be making sure
#      the inputs given are valid. The way I currently have the program assumes
#      the user will only input what each question requires i.e. a "y" or "n"
#      while asking if they own all the green properties. This is bad practice
#      to assume the user will follow everything I want him them to put in.
#      Also at first I had all my checks at the end of the program before moving
#      forward with any of the purchases. I later reorganized them to happen
#      throughout the program to minimize the amount of questions asked.
# 5. How long did it take for you to complete the assignment?
#      3 Hours

# Prompt if they own all the properties
own_all = input("Do you own all the green properties? (y/n) ")
# Must own all 3 properties to purchase a hotel
if own_all == "n":
    print("You cannot purchase a hotel until you own")
    print("\tall the properties of a given color group.")
    quit()

# Prompt for Pacific Ave
pac_ave = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
# Calculate the amount of houses needed at Pacific.
# If There's a hotel then no houses are needed
if pac_ave == 5:
    num_house_Pacific_need = 0
else:
    num_house_Pacific_need = 4 - pac_ave

# Prompt for North Carolina Ave
nc_ave = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
# Calculate the amount of houses needed at North Carolina.
# If There's a hotel then no houses are needed
if nc_ave == 5:
    num_house_NC_need = 0
else:
    num_house_NC_need = 4 - nc_ave

#Prompt for Pennsylvania Ave
pen_ave = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
# Only 1 Hotel allowed on a single property at a time
if pen_ave == 5:
    print("You cannot purchase a hotel if the property already has one.")
    quit()
elif (pac_ave == 5) and (pen_ave == 4):
    print("Swap Pacific's hotel with Pennsylvania's 4 houses.") 
    quit()
elif (nc_ave == 5) and (pen_ave == 4):
    print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
    quit()
else:
    # Calculate the amount of houses needed at Pennsylvania.
    # If There's a hotel then no houses are needed
    if pen_ave == 5:
        num_house_PA_need = 0
    else:
        num_house_PA_need = 4 - pen_ave

# Prompt for available Houses
num_house = int(input("How many houses are there to purchase? "))

# Prompt for available Hotels
num_hotel = int(input("How many hotels are there to purchase? "))
# There must be available Hotels in order to buy one
if num_hotel == 0:
    print("There are not enough hotels available for purchase at this time.")
    quit()

# Prompt for Cash
cash = int(input("How much cash do you have to spend? ")) 

# Add up the total amount of houses needed
houses_need = num_house_PA_need + num_house_NC_need + num_house_Pacific_need

# Each house and hotel is worth $200. We will buy 1 hotel
money_need = (houses_need * 200) + 200

# Enfforcing a few more rules
# Must have enough houses in the bank
if cash < money_need:
    print("You do not have sufficient funds to purchase a hotel at this time.")
    quit()
# Must have enough cash to make the purchase
elif num_house < houses_need:
    print("There are not enough houses available for purchase at this time.")
    quit()
# Otherwise if all the parameters are met...
else:
    print("This will cost $%d." % money_need)
    print("\tPurchase 1 hotel and %d house(s)." % houses_need)
    print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
    if num_house_NC_need:
        print("\tPut %d house(s) on North Carolina." % num_house_NC_need)
    if num_house_Pacific_need:
        print("\tPut %d house(s) on Pacific." % num_house_Pacific_need)