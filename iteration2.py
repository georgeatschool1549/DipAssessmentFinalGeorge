#George Robinson
#Iteration 2
#BDSC Cafe

food_price = ("2nd_food_menu.txt") # reads food menu drink
food_item = ("2nd_food_menu.txt") # reads food menu item
drink_price = ("2nd_drink_menu.txt") # reads drink menu price
drink_item = ("2nd_drink_menu.txt") # reads drink menu items

with open("2nd_food_menu.txt","r") as f: # reads files
    food_price = f.readlines()

with open("2nd_drink_menu.txt","r") as f: # reads files
    drink_price = f.readlines()

def confirmation(): # confirmation of order
    confirmation1 = input("Confirmation of order (Yes/No):")
    try:
        first_letter_conf = confirmation1[0] # first letter conf is the first letter of the input so if user types yes it will be y
    except IndexError:
        print("You must enter 'Yes' or 'No', please try again:")
        confirmation()

    if first_letter_conf.lower().strip() == "y": # if yes it says thanks for order
        print("Thanks for your order!")
        options()
    elif first_letter_conf.lower().strip() == "n": # if no it says order canceled
        print("Order canceled") 
        options()
    elif first_letter_conf.lower().strip() == "":
        print("Invalid, please try again:") # if unknown it will ask again
        confirmation()
    else:
        print("Invalid, please try again:")
        confirmation()

def options():
    print("1. Order Food \n2. Order Drink \n3. Order Food + Drink \n4. Exit") # prints options
    
    while True:
        choice = input("Please pick an option: ") # Ask user for an option
        try:
            choice_num = int(choice)  # converts choice into a number then runs the subsiquent code
            if choice_num == 1:
                main_food()
            elif choice_num == 2:
                main_drink()
            elif choice_num == 3:
                main()
            elif choice_num == 4:
                exit()
            else:
                print("Please enter a numerical value in the range of the objects.") # if unable to determine what the user wants to select it prints the statmetns 
                continue
            break
        except ValueError: # exepts the value error
            print("Please enter a numerical value in the range of the objects.")

def account():

    username_enter = input("Enter your username: ")
    if username_enter == account_name: # if the entry is correct from the stored password, it prints correct and gos onto the next function
        print("Correct!")
        options()
    elif username_enter != account_name:
        print("Incorrect! Please try again") # if incorrect it will try it again 
        account()

def main_food():
    print("The BDSC Cafe Menu: ")
    print("")
    print("Food:")
    print("")
    with open("2nd_food_menu.txt", "r") as f:
        contents = f.readlines()
        print(contents[0], contents[1], contents[2], contents[3], contents[4], contents[5], contents[6], contents[7]) # reads each line needed from the text file
        print("")

    f_menu = []
    with open("2nd_food_menu.txt","r") as f:
        f_menu = f.readlines()

    f_order_items = [] # sets the 
    f_order_total = 0
    while True:
        f_order = input("Enter your food order item number then click enter. Press enter when complete: ")
      
        if f_order == "": # if entered, breaks code 
            break
        try:
            f_number_order = int(f_order)
            f_number_order_final = f_number_order - 1
            f_number_order_final_ten = f_number_order_final+10 # Calculates what item thet have picked 
            if f_number_order_final <= 8:
                f_item = f_menu[f_number_order_final]
                f_price = f_menu[f_number_order_final_ten] # the price equals the line plus 10 of the item.
                print(f_price) # prints price and item
                print(f_item)
            else:
                print("Invalid item number. Please try again.") # if invalid it will ask again
                continue
            print("Added to order")
            f_order_items.append(f_item) # adds item to the f_order_items list
            f_order_total += float(f_price) # calculates the price
        except ValueError: # excepts the value error
            print("Invalid input. Please try again.")
            main_food()
    
    print("-----------------------------")
    print("Order Summary:")
    print("Food")
    for item in f_order_items: # prints the order history
        print(item)
    print(f"Total: ${f_order_total:.2f}")
    print("-----------------------------")

    confirmation()




def main_drink():

    print("Drinks:")
    print("")

    with open("2nd_drink_menu.txt", "r") as f:
        contents = f.readlines()
        print(contents[0], contents[1], contents[2], contents[3], contents[4], contents[5], contents[6], contents[7]) # pritns each of the drinks 
        print("")

    d_menu = []
    with open("2nd_drink_menu.txt","r") as f: # reads the text file of drink menu 
        d_menu = f.readlines()


    d_order_items = []
    d_order_total = 0
    while True:
        d_order = input("Enter your food order item number then click enter. Press enter when complete: ") # asks user for the desired option
      
        if d_order == "":
            break
        try:
            d_number_order = int(d_order)
            d_number_order_final = d_number_order - 1
            d_number_order_final_ten = d_number_order_final+10# Calculates what item thet have picked 
            if d_number_order_final <= 8:
                d_item = d_menu[d_number_order_final]
                d_price = d_menu[d_number_order_final_ten]# the price equals the line plus 10 of the item.
                print(d_price)# prints price and item
                print(d_item)
            else:
                print("Invalid item number. Please try again.") # if invalid it will ask again
                continue
            print("Added to order")
            d_order_items.append(d_item)# adds item to the d_order_items list
            d_order_total += float(d_price)# calculates the price
        except ValueError:
            print("Invalid input. Please try again.") # expects the value error and trys again
    print("-----------------------------")
    print("Order Summary:")
    print("Drink")
    for item in d_order_items: # prints the order total 
        print(item)
    print(f"Total: ${ d_order_total:.2f}")
    print("-----------------------------")

    confirmation()

def main():
    print("The BDSC Cafe Menu: ")
    print("")
    print("Food:")
    print("")
    with open("2nd_food_menu.txt", "r") as f: # reads the file
        contents = f.readlines()
        print(contents[0], contents[1], contents[2], contents[3], contents[4], contents[5], contents[6], contents[7]) # reads each line needed from the text file
        print("")

    f_menu = []
    with open("2nd_food_menu.txt","r") as f: # reads the file
        f_menu = f.readlines()

    f_order_items = []
    f_order_total = 0
    while True:
        f_order = input("Enter your food order item number then click enter. Press enter when complete: ") # gets the desired option from the user 
      
        if f_order == "": # if the user presses enter, it will break
            break
        try:
            f_number_order = int(f_order)
            f_number_order_final = f_number_order - 1 # finds the item from the text file
            f_number_order_final_ten = f_number_order_final+10 # gets the price from the text file
            if f_number_order_final <= 8:
                f_item = f_menu[f_number_order_final] # adds the item in the variable
                f_price = f_menu[f_number_order_final_ten] # Adds the price in the price variable
                print(f_price) # prints the items and price
                print(f_item)
            else:
                print("Invalid item number. Please try again.") # exepts invalid input and lets user trys again
                continue
            print("Added to order")
            f_order_items.append(f_item) # adds the item to the list
            f_order_total += float(f_price) # calculates the price
        except ValueError:
            print("Invalid input. Please try again.")  # exepts invalid input and lets user trys again
            main_food()


    print("Drinks:")
    print("")

    with open("2nd_drink_menu.txt", "r") as f:
        contents = f.readlines()
        print(contents[0], contents[1], contents[2], contents[3], contents[4], contents[5], contents[6], contents[7])# reads each line needed from the text file
        print("")

    d_menu = []
    with open("2nd_drink_menu.txt","r") as f: # reads the text file 
        d_menu = f.readlines()


    d_order_items = []
    d_order_total = 0
    while True:
        d_order = input("Enter your food order item number then click enter. Press enter when complete: ") # asks the user what item they will like
      
        if d_order == "": # if the input is an enter, it will break
            break
        try:
            d_number_order = int(d_order)
            d_number_order_final = d_number_order - 1 # finds the item from the text file
            d_number_order_final_ten = d_number_order_final+10 # gets the price from the text file
            if d_number_order_final <= 8:
                d_item = d_menu[d_number_order_final] # adds the item in the variable
                d_price = d_menu[d_number_order_final_ten] # Adds the price in the price variable
                print(d_price)# prints the items and price
                print(d_item)
            else:
                print("Invalid item number. Please try again.")# exepts invalid input and lets user trys again
                continue
            print("Added to order")
            d_order_items.append(d_item) # adds the drink item into the list 
            d_order_total += float(d_price) # calculates price
        except ValueError:
            print("Invalid input. Please try again.")# exepts invalid input and lets user trys again

    print("-----------------------------")
    print("Order Summary:")
    print("Food")
    for item in f_order_items: # prints the order summary 
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
account_name = input("Welcome, please enter your new username: ") # asks the user for their username
account()
