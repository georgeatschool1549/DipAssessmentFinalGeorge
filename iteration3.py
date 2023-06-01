#George Robinson
#Iteration 3
#BDSC Cafe
from tkinter import *  # imports all of the tkinter code 

root = Tk()  # sets the root as TK()
root.title("BDSC Cafe")  # sets title as BDSC Cafe 
root.geometry("400x950") # sets the size of window


with open("3rd_account.txt") as file: # opens the 3rd account text file 
    password_true = file.readline().strip() 


def clear_app_password():  # sets the password as a placeholder text, this is so that the user can reset the password.
    global password_true
    password_true = "!password_placeholder_text!"
    with open("3rd_account.txt", "w") as file:
        file.write(password_true)
    frame3.destroy()    # destroys the frame and goes back to frame 1
    frames1()




def frames1():
    global frame1
    frame1 = Frame(root)
    frame1.grid(row=0, column=0, sticky="nsew")


    lblPass = Label(frame1, text="Hello New User! \n Please create an account:") # asks user to create an account 
    lblPass.grid(row=0, column=0) 

    entryPass = Entry(frame1, show="*")  # entry box - replaces characters with * 
    entryPass.grid(row=1, column=0)

    lblPass = Label(frame1, text="Make sure to remember\n this password! We will \n ask you for it next\n time you sign in.") 
    lblPass.grid(row=2, column=0)

    lblEmpty = Label(frame1, text="")
    lblEmpty.grid(row=3, column=0)

    lblAge = Label(frame1, text="Please enter your age:")
    lblAge.grid(row=4, column=0)

    boxAge = Spinbox(frame1, from_=13,to=18, width=5) # spinbox gathers users age
    boxAge.grid(row=5, column=0)

    btnLogin = Button(frame1, text="Create Account", command=lambda: set_password(entryPass.get())) # when button is pressed it runs the code that writes the password
    btnLogin.grid(row=6, column=0)

def set_password(password): # this function makes it so that when the user enters their password, the code writes it into the password3.txt file
    with open("3rd_account.txt", "w") as file:
        file.write(password)

    global password_true
    password_true = password 
    frames2()   # runs next frame

def frames2(): # This frame asks for the password, so any returning users will have to enter their password before entering and viewing their acount naems and passwords
    global frame2
    frame2 = Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew")

    lblPass = Label(frame2, text="Password (App Sign In)")
    lblPass.grid(row=1, column=0)

    entryPass = Entry(frame2, show="*") # changes the viewable characters as a dot to hide what they are typing
    entryPass.grid(row=2, column=0)

    btnLogin = Button(frame2, text="LogIn", command=lambda: check_password(entryPass.get(), error_label)) # checks entry with the set password from the account text file
    btnLogin.grid(row=3, column=0)

    error_label = Label(frame2)
    error_label.grid(row=4, column=0, pady=10)


def orderfood():

    global frame4
    frame4 = Frame(root)
    frame4.grid(row=0, column=0, sticky="NSEW")

    lblTitle = Label(frame4, text="Order Food")
    lblTitle.grid(row=1, column=0)

    with open("3rd_food_menu.txt", "r") as f: #reads passwords
        data = f.read()

    text_box = Label(frame4, text=data)
    text_box.grid(row=2, column=0, sticky="NSEW")

    

    lblOptions = Label(frame4, text="Your options:")
    lblOptions.grid(row=3, column=0)

    

    chk_state1 = BooleanVar()
    chk_state1.set(False)
    chk1 = Checkbutton(frame4, text='Hotdog', var=chk_state1) # check box with name of item
    chk1.grid(column=0,row=4)

    chk_state2 = BooleanVar()
    chk_state2.set(False)
    chk2 = Checkbutton(frame4, text='Pie', var=chk_state2)# check box with name of item
    chk2.grid(column=0,row=5)

    chk_state3 = BooleanVar()
    chk_state3.set(False)
    chk3 = Checkbutton(frame4, text='Burger', var=chk_state3)# check box with name of item
    chk3.grid(column=0,row=6)

    chk_state4 = BooleanVar()
    chk_state4.set(False)
    chk4 = Checkbutton(frame4, text='Pizza', var=chk_state4)# check box with name of item
    chk4.grid(column=0,row=7)

    chk_state5 = BooleanVar()
    chk_state5.set(False)
    chk5 = Checkbutton(frame4, text='Sandwich', var=chk_state5)# check box with name of item
    chk5.grid(column=0,row=8)

    chk_state6 = BooleanVar()
    chk_state6.set(False)
    chk6 = Checkbutton(frame4, text='Hot Chips', var=chk_state6)# check box with name of item
    chk6.grid(column=0,row=9)

    chk_state7 = BooleanVar()
    chk_state7.set(False)
    chk7 = Checkbutton(frame4, text='Onion Rings', var=chk_state7)# check box with name of item
    chk7.grid(column=0,row=10)

    chk_state8 = BooleanVar()
    chk_state8.set(False)
    chk8 = Checkbutton(frame4, text='Wraps', var=chk_state8)# check box with name of item
    chk8.grid(column=0,row=11)

    def order_total_f():
        price1 = 0
        price2 = 0
        price3 = 0 # sets prices as 0, this will be changed depending on what the user selects
        price4 = 0
        price5 = 0
        price6 = 0
        price7 = 0
        price8 = 0

        if chk_state1.get() == True: # if the user sets a checkbox, it sets the above variables with the price in this if statment
            price1 = 2.0
        if chk_state2.get() == True:
            price2 = 4.50
        if chk_state3.get() == True:
            price3 = 6.0
        if chk_state4.get() == True:
            price4 = 6.0
        if chk_state5.get() == True:
            price5 = 3.20
        if chk_state6.get() == True:
            price6 = 4.0
        if chk_state7.get() == True:
            price7 = 3.0
        if chk_state8.get() == True:
            price8 = 4.0

        order_total = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 # adds the order total together 
        

        lblTotalTitle = Label(frame4, text="Your Order Total is($):")
        lblTotalTitle.grid(row=15, column=0, sticky=NSEW)

        emptySpace = Label(frame4, text="")
        emptySpace.grid(row=13, column=0, sticky=NSEW)

        emptySpace2 = Label(frame4, text="")
        emptySpace2.grid(row=14, column=0, sticky=NSEW)

        lblTotal = Label(frame4, text=order_total)
        lblTotal.grid(row=16, column=0, sticky=NSEW) # prints the order total 
    order_total_f()








    btnEnter = Button(frame4, text="Calculate Price", command=order_total_f) # pressing enter initates the price of the order total
    btnEnter.grid(column=0, row=12)


    lblTotal = Label(frame4, text= "Are you sure you want to Order?")
    lblTotal.grid(row=17, column=0)

    rad1 = Radiobutton(frame4, text='Yes', value=1) # radio buttons check weather the user wants to confirm their order
    rad1.grid(row=18, column=0)

    rad2 = Radiobutton(frame4, text='No', value=0)
    rad2.grid(row=19, column=0)


    btnClose = Button(frame4, text="Enter", command=frame4.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(column=0, row=20)

    
def order_drink():

    global frame5
    frame5 = Frame(root)
    frame5.grid(row=0, column=0, sticky="NSEW")

    lblTitle = Label(frame5, text="Order Drink")
    lblTitle.grid(row=1, column=0)

    with open("3rd_drink_menu.txt", "r") as f: #reads passwords
        data1 = f.read()

    text_box = Label(frame5, text=data1)
    text_box.grid(row=2, column=0, sticky="NSEW")

    

    lblOptions = Label(frame5, text="Your options:")
    lblOptions.grid(row=3, column=0)


    chk_state1 = BooleanVar()
    chk_state1.set(False)
    chk1 = Checkbutton(frame5, text='Water', var=chk_state1) # check box with name of item
    chk1.grid(column=0,row=4)

    chk_state2 = BooleanVar()
    chk_state2.set(False)
    chk2 = Checkbutton(frame5, text='Flavoured Water', var=chk_state2) # check box with name of item
    chk2.grid(column=0,row=5)

    chk_state3 = BooleanVar()
    chk_state3.set(False)
    chk3 = Checkbutton(frame5, text='Cola', var=chk_state3)# check box with name of item
    chk3.grid(column=0,row=6)

    chk_state4 = BooleanVar()
    chk_state4.set(False)
    chk4 = Checkbutton(frame5, text='Lemonade', var=chk_state4) # check box with name of item
    chk4.grid(column=0,row=7)

    chk_state5 = BooleanVar()
    chk_state5.set(False)
    chk5 = Checkbutton(frame5, text='Iced Chocolate', var=chk_state5)# check box with name of item
    chk5.grid(column=0,row=8)

    chk_state6 = BooleanVar()
    chk_state6.set(False)
    chk6 = Checkbutton(frame5, text='Hot Coffee', var=chk_state6) # check box with name of item
    chk6.grid(column=0,row=9)

    chk_state7 = BooleanVar()
    chk_state7.set(False)
    chk7 = Checkbutton(frame5, text='Hot Chocolate', var=chk_state7) # check box with name of item
    chk7.grid(column=0,row=10)



    def order_total_d():
        price1 = 0
        price2 = 0
        price3 = 0
        price4 = 0
        price5 = 0 # sets the price as zero however this will be changed according to what the user sets
        price6 = 0
        price7 = 0

        if chk_state1.get() == True:# if the user sets a checkbox, it sets the above variables with the price in this if statment
            price1 = 1.0
        if chk_state2.get() == True:
            price2 = 1.5
        if chk_state3.get() == True:
            price3 = 4.0
        if chk_state4.get() == True:
            price4 = 3.5
        if chk_state5.get() == True:
            price5 = 4.0
        if chk_state6.get() == True:
            price6 = 4.0
        if chk_state7.get() == True:
            price7 = 4.0


        order_total = price1 + price2 + price3 + price4 + price5 + price6 + price7 # calculates the total price 
        

        lblTotalTitle = Label(frame5, text="Your Order Total is($):")
        lblTotalTitle.grid(row=15, column=0, sticky=NSEW)

        emptySpace = Label(frame5, text="")
        emptySpace.grid(row=13, column=0, sticky=NSEW)

        emptySpace2 = Label(frame5, text="")
        emptySpace2.grid(row=14, column=0, sticky=NSEW)

        lblTotal = Label(frame5, text=order_total) # prints the total price 
        lblTotal.grid(row=16, column=0, sticky=NSEW)
    order_total_d()








    btnEnter = Button(frame5, text="Calculate Price", command=order_total_d)
    btnEnter.grid(column=0, row=12)


    lblTotal = Label(frame5, text= "Are you sure you want to Order?")
    lblTotal.grid(row=17, column=0)

    rad1 = Radiobutton(frame5, text='Yes', value=1) # radio buttons represents the order confirmations
    rad1.grid(row=18, column=0)

    rad2 = Radiobutton(frame5, text='No', value=0)
    rad2.grid(row=19, column=0)


    btnClose = Button(frame5, text="Enter", command=frame5.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(column=0, row=20)

def food_drink():
    global frame6
    frame6 = Frame(root)
    frame6.grid(row=0, column=0, sticky="NSEW")

    lblTitle = Label(frame6, text="Order Food and Drink")
    lblTitle.grid(row=1, column=0)

    with open("3rd_drink_menu.txt", "r") as f: #reads passwords
        data2 = f.read()

    text_box = Label(frame6, text=data2)
    text_box.grid(row=1, column=0, sticky="NSEW")


    with open("3rd_food_menu.txt", "r") as f: #reads passwords
        data = f.read()

    text_box = Label(frame6, text=data)
    text_box.grid(row=1, column=1, sticky="NSEW")

    

    

    lblOptions = Label(frame6, text="Your options:")
    lblOptions.grid(row=2, column=0)


    chk_state1 = BooleanVar()
    chk_state1.set(False)
    chk1 = Checkbutton(frame6, text='Water', var=chk_state1) # check box with name of item
    chk1.grid(column=0,row=3)

    chk_state2 = BooleanVar()
    chk_state2.set(False)
    chk2 = Checkbutton(frame6, text='Flavoured Water', var=chk_state2) # check box with name of item
    chk2.grid(column=0,row=4)

    chk_state3 = BooleanVar()
    chk_state3.set(False)
    chk3 = Checkbutton(frame6, text='Cola', var=chk_state3) # check box with name of item
    chk3.grid(column=0,row=5)

    chk_state4 = BooleanVar()
    chk_state4.set(False)
    chk4 = Checkbutton(frame6, text='Lemonade', var=chk_state4) # check box with name of item
    chk4.grid(column=0,row=6)

    chk_state5 = BooleanVar()
    chk_state5.set(False)
    chk5 = Checkbutton(frame6, text='Iced Chocolate', var=chk_state5) # check box with name of item
    chk5.grid(column=0,row=7)

    chk_state6 = BooleanVar()
    chk_state6.set(False)
    chk6 = Checkbutton(frame6, text='Hot Coffee', var=chk_state6) # check box with name of item
    chk6.grid(column=0,row=8)

    chk_state7 = BooleanVar()
    chk_state7.set(False)
    chk7 = Checkbutton(frame6, text='Hot Chocolate', var=chk_state7) # check box with name of item
    chk7.grid(column=0,row=9)


    lblOptions = Label(frame6, text="Your Options:")
    lblOptions.grid(row=2, column=1)

    

    chk_state8 = BooleanVar()
    chk_state8.set(False)
    chk8 = Checkbutton(frame6, text='Hotdog', var=chk_state8) # check box with name of item
    chk8.grid(column=1,row=3)

    chk_state9 = BooleanVar()
    chk_state9.set(False)
    chk9 = Checkbutton(frame6, text='Pie', var=chk_state9) # check box with name of item
    chk9.grid(column=1,row=4)

    chk_state10 = BooleanVar()
    chk_state10.set(False)
    chk10 = Checkbutton(frame6, text='Burger', var=chk_state10) # check box with name of item
    chk10.grid(column=1,row=5)

    chk_state11 = BooleanVar()
    chk_state11.set(False)
    chk11 = Checkbutton(frame6, text='Pizza', var=chk_state11) # check box with name of item
    chk11.grid(column=1,row=6) 

    chk_state12 = BooleanVar()
    chk_state12.set(False)
    chk12 = Checkbutton(frame6, text='Sandwich', var=chk_state12) # check box with name of item
    chk12.grid(column=1,row=7)

    chk_state13 = BooleanVar()
    chk_state13.set(False)
    chk13 = Checkbutton(frame6, text='Hot Chips', var=chk_state13) # check box with name of item
    chk13.grid(column=1,row=8)

    chk_state14 = BooleanVar()
    chk_state14.set(False)
    chk14 = Checkbutton(frame6, text='Onion Rings', var=chk_state14) # check box with name of item
    chk14.grid(column=1,row=9)

    chk_state15 = BooleanVar()
    chk_state15.set(False)
    chk15 = Checkbutton(frame6, text='Wraps', var=chk_state15) # check box with name of item
    chk15.grid(column=1,row=10) 

    def order_total_f():
        price1 = 0
        price2 = 0
        price3 = 0
        price4 = 0
        price5 = 0
        price6 = 0 # sets the price as 0 but this will change depending on what the user sets as an option
        price7 = 0
        price8 = 0
        price9 = 0
        price10 = 0
        price11 = 0
        price12 = 0
        price13 = 0
        price14 = 0
        price15 = 0

        if chk_state1.get() == True:# if the user sets a checkbox, it sets the above variables with the price in this if statment
            price1 = 2.0
        if chk_state2.get() == True:
            price2 = 4.50
        if chk_state3.get() == True:
            price3 = 6.0
        if chk_state4.get() == True:
            price4 = 6.0
        if chk_state5.get() == True:
            price5 = 3.20
        if chk_state6.get() == True:
            price6 = 4.0
        if chk_state7.get() == True:
            price7 = 3.0
        if chk_state8.get() == True:
            price8 = 4.0
        if chk_state9.get() == True:
            price9 = 4.0
        if chk_state10.get() == True:
            price10 = 4.0
        if chk_state11.get() == True:
            price11 = 4.0
        if chk_state12.get() == True:
            price12 = 4.0
        if chk_state13.get() == True:
            price13 = 4.0
        if chk_state14.get() == True:
            price14 = 4.0
        if chk_state15.get() == True:
            price15 = 4.0

        order_total = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 + price9 + price10 + price11 + price12 + price13 + price14 + price15 # calculates the total price 
        
        emptySpace = Label(frame6, text="")
        emptySpace.grid(row=11, column=0, sticky=NSEW)

        lblTotalTitle = Label(frame6, text="Your Order Total is($):")
        lblTotalTitle.grid(row=12, column=0, sticky=NSEW)

        lblTotal = Label(frame6, text=order_total) # this prints the order total 
        lblTotal.grid(row=14, column=0, sticky=NSEW)
    order_total_f()



    btnEnter = Button(frame6, text="Calculate Price", command=order_total_f)
    btnEnter.grid(column=0, row=15)


    lblTotal = Label(frame6, text= "Are you sure you want to Order?")
    lblTotal.grid(row=16, column=0)

    rad1 = Radiobutton(frame6, text='Yes', value=1) # this acts as the order confirmaton 
    rad1.grid(row=17, column=0)

    rad2 = Radiobutton(frame6, text='No', value=0)
    rad2.grid(row=18, column=0)


    btnClose = Button(frame6, text="Enter", command=frame6.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(column=0, row=19)

def exit_p():
    exit()



def check_password(password, error_label): # this is the main frame where the user can add passwords, view passwords, remove passwords and change app password
    global frame3
    if password == password_true:
        frame3 = Frame(root)
        frame3.grid(row=0, column=0, sticky="NSEW")
     
        btnClearAppPassword = Button(frame3, text="Clear Your App Password", command=clear_app_password) # this is the frame where the user can select what options that
        btnClearAppPassword.grid(row=0, column=1)

        btnOrderFood = Button(frame3, text="Order Food", command=orderfood)
        btnOrderFood.grid(row=1, column=1)

        btnOrderDrink = Button(frame3, text="Order Drink", command=order_drink)
        btnOrderDrink.grid(row=2, column=1)

        btnOrderFoodAndDrink = Button(frame3, text="Order Food and Drink", command=food_drink)
        btnOrderFoodAndDrink.grid(row=3, column=1)

        btnExit = Button(frame3, text="Exit", command=exit_p)
        btnExit.grid(row=4, column=1)



    else:
        error_label.config(text="Password is incorrect!\n Please try again")  #shows incorrect password text if they enter wrong password 


if password_true == "!password_placeholder_text!": #this is the actual main code it decides what function to run depending on the contents of the txt file. If the file has the placeholder text,it will run the first frame otherwise it will run the second frmae
    frames1()
else:
    frames2()

root.mainloop() # ends the main loop
