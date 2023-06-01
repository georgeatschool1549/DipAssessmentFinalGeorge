#George Robinson
#Iteration 1
#BDSC Cafe



# This is a dictionary that stores information. The information stored in thius dictionary is the text that displays the menu and the prices associated with it.
food = {0 : ["1. Hot Dog","$", 2.00], 1 : ["2. Pie","$", 4.50], 2 : ["3. Burger","$", 6.00], 3 : ["4. Pizza","$", 6.00], 4 : ["5. Sandwich","$", 3.20], 5 : ["6. Hot Chips","$", 4.00], 6 : ["7. Onion Rings","$", 3.00], 7 : ["8. Wraps","$", 4.00]} 
drinks = {0 : ["1. Water","$", 1.00], 1 : ["2. Flavoured Water","$", 1.50], 2 : ["3. Cola","$", 4.00], 3 : ["4. Lemonade","$", 3.50], 4 : ["5. Iced Chocolate","$", 4.00], 5 : ["6. Hot Coffee","$", 4.00], 6 : ["7. Hot Chocolate","$", 4.00]}
# This function provides options for the user. This means that they can pick between order food/drink/food and drink/exit.
def options():
    print("1. Order Food \n2. Order Drink \n3. Order Food + Drink \n4. Exit") #\n means that it is a new line.
    try:
        choice = int(input("Please pick an option :")) # int converts the entry into an interger. 
        if choice == 1:
            main_food()
        if choice == 2:
            main_drink()
        if choice == 3:
            main()
        if choice == 4:
            exit()
        else:
            print("Invalid, please try again...")
            options() # runs the program again if the entry is invalid. 
    except ValueError:
        print("Invalid input, please try again - you will need to use numbers.") # runs the program again if the entry is invalid. 
        options()
#This function is a confirmation function that asks the user if they are sure they want to order.
def confirmation():
    confirmation1 = input("Confirmation of order (Yes/No):")
    first_letter_conf = confirmation1[0]
#.stip and .lower removes uppercases and spaces from the users input. It then checks weather the user types yes or no by checking the first letter. SO the user will be able to say Yeah, Nah, Yup, e.t.c
    if first_letter_conf.lower().strip() == "y": 
        print("Thanks for your order!")
        options()
    elif first_letter_conf.lower().strip() == "n":
        print("Order canceled") 
        options()
    else: # If there is some issue with the entry (e.g: enters a number), it will say invalid please try again. It then runs the code agian.
        print("Invalid, please try again:")
        confirmation()


    
def account(): # this function asks the user for their username. If the user name mathes with the account_name variable, it lets them in. 
    username_enter = input("Enter your username: ")
    if username_enter == account_name:
        print("Correct!")
        options()
    elif username_enter != account_name: # if the input does not match the account name, it comes up with an image saying
        print("Incorrect! Please try again")
        account()

def main_food(): # this is the main function that runs the food frame. This means that the user can only order food here. 
    print("The BDSC Cafe Menu: ")
    print("")
    print("Food:")
    print("")
    for i in range (len(food)): 
        print(food[i]) # This code prints each item in the food dictionary. 
    print("") # prints new line

    f_order_items = [] # sets items in list as none. 
    f_order_total = 0 # sets the order total as 0 .
    while True:
        f_order = input("Enter your food order item number then click enter. If done type 0: ") # asks the users options. 
        f_order_final = int(f_order) - 1 #Converts the input into an int. Then minuses one as computing theory states that the start of a list starts at 0. 
        
        if f_order_final == -1: # If the user types 0 (will end up as -1), it breaks the code and returns to options. 
            break
        try: # Try and except allows for errors. 
            f_number_order = f_order_final 
            if f_number_order <= 8: # if the number entered is less than 8:
                f_item = food[f_number_order][0] # sets f_item as the option selected by user from the food menu.
                f_price = food[f_number_order][2] # Sets the f_price as the price associated with the item from the above code. 
            else:
                print("Invalid item number. Please try again.") # prints the invalid statment and continues to try agian. 
                continue
            print("Added to order") # if the order was successful it prints a added to order stamtent.
            f_order_items.append(f_item) # adds to the list, f_order_items
            f_order_total =+ f_price
        except ValueError:
            print("Invalid input. Please try again.") # exepts value error and prints an error stamtent. Allows the user to try again. 
            main_food()
    
    print("-----------------------------")
    print("Order Summary:")
    print("Food")
    for item in f_order_items: # Prints each item from the list. 
        print(item)
    print(f"Total: ${f_order_total:.2f}") # prints the order total 
    print("-----------------------------")

    confirmation()
def main_drink():# this is the main function that runs the drink frame. This means that the user can only order food here. 

    print("Drinks:")
    print("")
    for i in range (len(drinks)):
        print(*drinks[i]) # This code prints each item in the food dictionary. 
    print("")

    d_order_items = [] # Sets the items in the lsit as none, items will be aded to this later. 
    d_order_total = 0 # This sets the order total as 0, this price will be uptaded as more items are added 
    while True:
        d_order = input("Enter your drink order item number then click enter. If done type 0: ") # Asks user for their option. 
        d_order_final = int(d_order) - 1  
        if d_order_final == -1: # If the user types 0 (will end up as -1), it breaks the code and returns to options. 
            break
        try:
            d_number_order = d_order_final
            if d_number_order <= 8: # If the number is less than 8, the following code will run
                d_item = drinks[d_number_order][0] # sets the drink items as the entered number from the list
                d_price = drinks[d_number_order][2] # sets the price as the number asociated with the selected item.
            else:
                print("Invalid item number. Please try again.") # fail safe if the code doesnt work.
                continue
            print("Added to order")
            d_order_items.append(d_item) # adds the items into the empty list 
            d_order_total += d_price
        except ValueError:
            print("Invalid input. Please try again.")
            main_drink()

    print("-----------------------------")
    print("Order Summary:")
    print("Drink")
    for item in d_order_items:
        print(item) # pritns each item so the user can see their order summary. 
    print(f"Total: ${ d_order_total:.2f}") 
    print("-----------------------------")

    confirmation()

# the code below displays the food and drink menu in one. This is so that the user doesnt have to do two orders if they want food and drink. 
def main():
    print("The BDSC Cafe Menu: ")
    print("")
    print("Food:")
    print("")
    for i in range (len(food)):
        print(*food[i])
    print("")

    f_order_items = []
    f_order_total = 0
    while True:
        f_order = input("Enter your food order item number then click enter. If done type 0: ")
        f_order_final = int(f_order) - 1
        
        if f_order_final == -1:
            break
        try:
            f_number_order = f_order_final
            if f_number_order <= 8:
                f_item = food[f_number_order][0]
                f_price = food[f_number_order][2] # calculates the price 
            else:
                print("Invalid item number. Please try again.")
                continue
            print("Added to order")
            f_order_items.append(f_item) # adds the f_item to the order items list 
            f_order_total += f_price
        except ValueError:
            print("Invalid input. Please try again.")
            main()


    print("Drinks:")
    print("")
    for i in range (len(drinks)):
        print(*drinks[i])
    print("")

    d_order_items = []
    d_order_total = 0
    while True:
        d_order = input("Enter your drink order item number then click enter. If done type 0: ")
        d_order_final = int(d_order) - 1
        if d_order_final == -1:
            break
        try:
            d_number_order = d_order_final
            if d_number_order <= 8:
                d_item = drinks[d_number_order][0] # calculates the prince from above
                d_price = drinks[d_number_order][2]
            else:
                print("Invalid item number. Please try again.")
                continue
            print("Added to order")
            d_order_items.append(d_item)
            d_order_total += d_price
        except ValueError:
            print("Invalid input. Please try again.")
            main()

    print("-----------------------------")
    print("Order Summary:")
    print("Food")
    for item in f_order_items: # prints order summary
        print(item)
    print("Drink")
    for item in d_order_items:
        print(item)
    print(f"Total: ${f_order_total + d_order_total:.2f}")
    print("-----------------------------")

    confirmation()


print("--------------------------")
print("Welcome to the BDSC Cafe!")
print("--------------------------")
account_name = input("Welcome, please enter your new username: ")
account()
