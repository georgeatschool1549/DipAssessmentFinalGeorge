#George Robinson
#Iteration 4
#BDSC Cafe

from tkinter import * # imports all of tkinter
from PIL import Image, ImageTk # imputs tkinter image 
root = Tk() #sets tk as root
root.title("BDSC Cafe") # name of program
root.geometry("600x500") # sets geometry of window
root.configure(bg="AntiqueWhite2") # configures the background of the app
unpw = {} 
with open("4th_account.txt") as file: # reads the 4th account text file 
    password_true = file.readline().strip()  # strps the password from spaces and capitals 

def logout(): 
    frame3.destroy()    # destroys the frame 3 frame and displays the first frame
    frames1()

def frames1():
    global frame1
    frame1 = Frame(root)
    frame1.grid(row=0, column=0, sticky="nsew")
    frame1.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame1, text="")
    emptySpace.grid(pady=20, padx=225) 
    emptySpace.configure(bg="AntiqueWhite2")

    img = Image.open("bdsc.png") # displays an image called bdsc
    img = img.resize((100, 100))
    img1 = ImageTk.PhotoImage(img)
    la_bel = Label(frame1, image=img1)
    la_bel.image = img1 # displayed in this label so it can be adjusted. This image is the bdsc logo
    la_bel.grid(pady=0, padx=225)
    la_bel.configure(bg="AntiqueWhite2")

    lblPass = Label(frame1, text="BDSC Cafe")
    lblPass.grid(pady=0, padx=225) 
    lblPass.configure(fg="brown4", bg="AntiqueWhite2")

    btnCreateAccount = Button(frame1, bg="CadetBlue1", fg="black", text="Create Account", command=create_account)  # This button runs the create account function
    btnCreateAccount.grid(pady=0, padx=225)
    btnCreateAccount.configure()

    btnLogIn = Button(frame1, text="Log In", command=frames2) # this button runs the frams2 command 
    btnLogIn.grid(pady=0, padx=225)
    btnLogIn.configure(bg="AntiqueWhite2", fg="black")

def create_account():
    global frame10
    frame10 = Frame(root)
    frame10.grid(row=0, column=0, sticky="nsew")
    frame10.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame10, text="")
    emptySpace.grid(pady=15, padx=300)
    emptySpace.configure(bg="AntiqueWhite2")

    lblUser = Label(frame10, bg="AntiqueWhite2", fg="black", text="Welcome to the BDSC Cafe! \n Please create an account Username:")
    lblUser.grid(pady=0, padx=0)

    entryUser = Entry(frame10, fg="black")
    entryUser.grid(pady=0, padx=0)

    lblPass = Label(frame10, bg="AntiqueWhite2", fg="black", text="Please create an account Password:")
    lblPass.grid(pady=0, padx=0)

    entryPass = Entry(frame10, fg="black", show="*") # entry box for the user to enter their password, will be protected by a *
    entryPass.grid(pady=0, padx=0)

    lblEmpty = Label(frame10, bg="AntiqueWhite2", fg="black", text="")
    lblEmpty.grid(pady=0, padx=0)

    lblAge = Label(frame10, bg="AntiqueWhite2", fg="black", text="Please enter your age:") # asks user for their age
    lblAge.grid(pady=0, padx=0)

    boxAge = Spinbox(frame10, bg="AntiqueWhite2", fg="black", from_=0, to=130, width=5) # spinbox is used to display the age 
    boxAge.grid(pady=0, padx=0)

    age_error_label = Label(frame10, bg="AntiqueWhite2", fg="black")
    age_error_label.grid(pady=0, padx=0)
    
    def on_create_account():
        age_v = int(boxAge.get())

        if age_v <= 12 or age_v >= 19:
            age_error_label.config(text="You must be High School Age (13-18)") # if the age is not in the allowed range, the configure code will display the text
        else:
            set_password(entryUser.get(), entryPass.get()) # if the age is in the range it runs the set_password function 

        return

    btnLogin = Button(frame10, bg="AntiqueWhite2", fg="black", text="Create Account", command=on_create_account) # log in button
    btnLogin.grid(pady=0, padx=0)

    btnBack = Button(frame10, bg="AntiqueWhite2", fg="black", text="Back", command=frames1) # back button 
    btnBack.grid(pady=0, padx=0)

def set_password(entryUser, entryPass):
    with open("4th_account.txt", "a") as file: # adds the password and username set by user into the 4th account text files 
        file.write(entryUser + entryPass + "\n")
    frames2()



def frames2(): # This frame asks for the password, so any returning users will have to enter their password before entering and viewing their acount naems and passwords
    global frame2
    frame2 = Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew")
    frame2.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame2, text="")
    emptySpace.grid(pady=20, padx=225) 
    emptySpace.configure(bg="AntiqueWhite2")

    lblUser = Label(frame2, bg="AntiqueWhite2", fg="black", text="Username")
    lblUser.grid(pady=0, padx=200)

    entryUser1 = Entry(frame2, fg="black") # changes the viewable characters as a dot to hide what they are typing
    entryUser1.grid(pady=0, padx=200)

    lblPass = Label(frame2, bg="AntiqueWhite2", fg="black", text="Password")
    lblPass.grid(pady=0, padx=200)

    entryPass1 = Entry(frame2, fg="black", show="*") # changes the viewable characters as a dot to hide what they are typing
    entryPass1.grid(pady=0, padx=200)

    btnLogin = Button(frame2, bg="AntiqueWhite2", fg="black", text="Log In", command=lambda: check_password(entryUser1.get(), entryPass1.get(), error_label)) # log in button runs the check password function
    btnLogin.grid(pady=0, padx=200)

    error_label = Label(frame2, fg="black", bg="AntiqueWhite2")
    error_label.grid(pady=0, padx=200)

    btnBack = Button(frame2, bg="AntiqueWhite2", fg="black", text="Back", command=frames1) #back button runs the frames1 button
    btnBack.grid(pady=0, padx=200)

def orderfood():
    global frame4
    frame4 = Frame(root)
    frame4.grid(row=0, column=0, sticky="NSEW")
    frame4.configure(bg="AntiqueWhite2")

    lblTitle = Label(frame4, bg="AntiqueWhite2", fg="black", text="Order Food")
    lblTitle.grid(pady=0, padx=100)
    
    lblOptions = Label(frame4, fg="black", bg="AntiqueWhite2", text="Your options:")
    lblOptions.grid(pady=0, padx=0)

    chk_state1 = BooleanVar()
    chk_state1.set(False)
    chk1 = Checkbutton(frame4, fg="black", bg="AntiqueWhite2", text='Hotdog | $2.00', var=chk_state1) # check box with name of item
    chk1.grid(pady=0, padx=0)

    boxq1 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq1.grid(pady=0, padx=0)

    chk_state2 = BooleanVar()
    chk_state2.set(False)
    chk2 = Checkbutton(frame4, fg="black", bg="AntiqueWhite2", text='Pie | $4.50', var=chk_state2) # check box with name of item
    chk2.grid(pady=0, padx=0)

    boxq2 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq2.grid(pady=0, padx=0)


    chk_state3 = BooleanVar()
    chk_state3.set(False)
    chk3 = Checkbutton(frame4, fg="black", bg="AntiqueWhite2",  text='Burger | $6.00', var=chk_state3) # check box with name of item
    chk3.grid(pady=0, padx=0)

    boxq3 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5)# spin box sets quantity of item
    boxq3.grid(pady=0, padx=0)

    chk_state4 = BooleanVar()
    chk_state4.set(False)
    chk4 = Checkbutton(frame4, fg="black",  bg="AntiqueWhite2", text='Pizza | $6.00', var=chk_state4) # check box with name of item
    chk4.grid(pady=0, padx=0)

    boxq4 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5)
    boxq4.grid(pady=0, padx=0)

    chk_state5 = BooleanVar()
    chk_state5.set(False)
    chk5 = Checkbutton(frame4, fg="black",  bg="AntiqueWhite2", text='Sandwich | $3.20', var=chk_state5) # check box with name of item
    chk5.grid(pady=0, padx=0)

    boxq5 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq5.grid(pady=0, padx=0)

    chk_state6 = BooleanVar()
    chk_state6.set(False)
    chk6 = Checkbutton(frame4, fg="black",  bg="AntiqueWhite2", text='Hot Chips | $4.00', var=chk_state6) # check box with name of item
    chk6.grid(pady=0, padx=0)

    boxq6 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq6.grid(pady=0, padx=0)

    chk_state7 = BooleanVar()
    chk_state7.set(False)
    chk7 = Checkbutton(frame4, fg="black",  bg="AntiqueWhite2", text='Onion Rings | $3.00', var=chk_state7) # check box with name of item
    chk7.grid(pady=0, padx=0)

    boxq7 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq7.grid(pady=0, padx=0)

    chk_state8 = BooleanVar()
    chk_state8.set(False)
    chk8 = Checkbutton(frame4, fg="black",  bg="AntiqueWhite2", text='Wraps | $4.00', var=chk_state8) # check box with name of item
    chk8.grid(pady=0, padx=0)

    boxq8 = Spinbox(frame4, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq8.grid(pady=0, padx=0)

    error_lbl = Label(frame4, bg="AntiqueWhite2", fg="black")
    error_lbl.grid(pady=0, padx=0)

    def order_total_f():
        try:
            price1 = 0
            price2 = 0
            price3 = 0
            price4 = 0
            price5 = 0 # sets the price to 0 dollars 
            price6 = 0
            price7 = 0
            price8 = 0

            if chk_state1.get() == True:
                price1 = 2.0 * int(boxq1.get()) # if the user sets a checkbox, it sets the above variables with the price multiplied by the quantity in this if statment
            if chk_state2.get() == True:
                price2 = 4.50 * int(boxq2.get())
            if chk_state3.get() == True:
                price3 = 6.0 * int(boxq3.get())
            if chk_state4.get() == True:
                price4 = 6.0 * int(boxq4.get())
            if chk_state5.get() == True:
                price5 = 3.20 * int(boxq5.get())
            if chk_state6.get() == True:
                price6 = 4.0 * int(boxq6.get())
            if chk_state7.get() == True:
                price7 = 3.0 * int(boxq7.get())
            if chk_state8.get() == True:
                price8 = 4.0 * int(boxq8.get())

            order_total = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8

            lblTotalTitle = Label(frame4, fg="black",  bg="AntiqueWhite2", text="Your Order Total is($):")
            lblTotalTitle.grid(row=1, column=2, pady=0, padx=25, sticky=NSEW)


            lblTotal = Label(frame4, fg="black",  bg="AntiqueWhite2", text=order_total)
            lblTotal.grid(row=2, column=2, pady=0, padx=25, sticky=NSEW)
        except ValueError:
            error_lbl.configure(text="There was an error with\n your quantities, please enter numbers only.")
    order_total_f()

    btnEnter = Button(frame4, fg="black",  bg="AntiqueWhite2", text="Calculate Price", command=order_total_f)
    btnEnter.grid(row=3, column=2, pady=0, padx=25)

    lblTotal = Label(frame4, fg="black",  bg="AntiqueWhite2", text= "Are you sure you want to Order?")
    lblTotal.grid(row=4, column=2, pady=0, padx=25)


    rad1 = Radiobutton(frame4, fg="black", bg="AntiqueWhite2", text='Yes', value=1)
    rad1.grid(row=5, column=2, pady=0, padx=25)

    rad2 = Radiobutton(frame4, fg="black",  bg="AntiqueWhite2", text='No', value=0)
    rad2.grid(row=6, column=2, pady=0, padx=25)
    

    btnClose = Button(frame4, fg="black",  bg="AntiqueWhite2", text="Enter", command=frame4.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(row=7, column=2, pady=0, padx=25)

def order_drink():
    global frame5
    frame5 = Frame(root)
    frame5.grid(row=0, column=0, sticky="NSEW")
    frame5.configure(bg="AntiqueWhite2")

    lblTitle = Label(frame5, fg="black",  bg="AntiqueWhite2", text="Order Drink")
    lblTitle.grid(pady=0, padx=100)
    
    lblOptions = Label(frame5, fg="black",  bg="AntiqueWhite2", text="Your options:")
    lblOptions.grid(pady=0, padx=0)

    chk_state1 = BooleanVar()
    chk_state1.set(False)
    chk1 = Checkbutton(frame5, fg="black", bg="AntiqueWhite2", text='Water | $1.00', var=chk_state1) # check box with name of item
    chk1.grid(pady=0, padx=0)

    boxq1 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq1.grid(pady=0, padx=0)

    chk_state2 = BooleanVar()
    chk_state2.set(False)
    chk2 = Checkbutton(frame5, fg="black",  bg="AntiqueWhite2", text='Flavoured Water | $1.50', var=chk_state2) # check box with name of item
    chk2.grid(pady=0, padx=0)

    boxq2 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq2.grid(pady=0, padx=0)

    chk_state3 = BooleanVar()
    chk_state3.set(False)
    chk3 = Checkbutton(frame5,fg="black",   bg="AntiqueWhite2", text='Cola | $4.00', var=chk_state3) # check box with name of item
    chk3.grid(pady=0, padx=0)

    boxq3 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq3.grid(pady=0, padx=0)

    chk_state4 = BooleanVar()
    chk_state4.set(False)
    chk4 = Checkbutton(frame5, fg="black",  bg="AntiqueWhite2", text='Lemonade | $3.50', var=chk_state4) # check box with name of item
    chk4.grid(pady=0, padx=0)

    boxq4 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq4.grid(pady=0, padx=0)

    chk_state5 = BooleanVar()
    chk_state5.set(False)
    chk5 = Checkbutton(frame5, fg="black",  bg="AntiqueWhite2", text='Iced Chocolate | $4.00', var=chk_state5) # check box with name of item
    chk5.grid(pady=0, padx=0)

    boxq5 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq5.grid(pady=0, padx=0)

    chk_state6 = BooleanVar()
    chk_state6.set(False)
    chk6 = Checkbutton(frame5, fg="black",   bg="AntiqueWhite2", text='Hot Coffee | $4.00', var=chk_state6) # check box with name of item
    chk6.grid(pady=0, padx=0)

    boxq6 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq6.grid(pady=0, padx=0)

    chk_state7 = BooleanVar()
    chk_state7.set(False)
    chk7 = Checkbutton(frame5, fg="black",  bg="AntiqueWhite2", text='Hot Chocolate | $4.00', var=chk_state7) # check box with name of item
    chk7.grid(pady=0, padx=0)

    boxq7 = Spinbox(frame5, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq7.grid(pady=0, padx=0)

    error_lbl = Label(frame5, bg="AntiqueWhite2", fg="black")
    error_lbl.grid(pady=0, padx=0)

    def order_total_d():
        try:
            price1 = 0
            price2 = 0
            price3 = 0
            price4 = 0
            price5 = 0# sets the price to 0 dollars 
            price6 = 0
            price7 = 0

            if chk_state1.get() == True:
                price1 = 1.0 * int(boxq1.get())
            if chk_state2.get() == True:
                price2 = 1.5 * int(boxq2.get()) # if the user sets a checkbox, it sets the above variables with the price multiplied by the quantity in this if statment
            if chk_state3.get() == True:
                price3 = 4.0 * int(boxq3.get())
            if chk_state4.get() == True:
                price4 = 3.5 * int(boxq4.get())
            if chk_state5.get() == True:
                price5 = 4.0 * int(boxq5.get())
            if chk_state6.get() == True:
                price6 = 4.0 * int(boxq6.get())
            if chk_state7.get() == True:
                price7 = 4.0 * int(boxq7.get())
            
            order_total = price1 + price2 + price3 + price4 + price5 + price6 + price7

            lblTotalTitle = Label(frame5, fg="black",  bg="AntiqueWhite2", text="Your Order Total is($):")
            lblTotalTitle.grid(row=0, column=2, pady=0, padx=25, sticky=NSEW)

            lblTotal = Label(frame5, fg="black",  bg="AntiqueWhite2", text=order_total)
            lblTotal.grid(row=1, column=2, pady=0, padx=25, sticky=NSEW)

        except ValueError:
            error_lbl.configure(text="There was an error with\n your quantities, please enter numbers only.")
    
    order_total_d()

    btnEnter = Button(frame5, fg="black",  bg="AntiqueWhite2", text="Calculate Price", command=order_total_d)
    btnEnter.grid(row=2, column=2, pady=0, padx=25)

    lblTotal = Label(frame5, fg="black",  bg="AntiqueWhite2", text= "Are you sure you want to Order?")
    lblTotal.grid(row=3, column=2, pady=0, padx=25)

    rad1 = Radiobutton(frame5, fg="black",  bg="AntiqueWhite2", text='Yes', value=1)
    rad1.grid(row=4, column=2, pady=0, padx=25)

    rad2 = Radiobutton(frame5, fg="black",  bg="AntiqueWhite2", text='No', value=0)
    rad2.grid(row=5, column=2, pady=0, padx=25)


    btnClose = Button(frame5, fg="black",  bg="AntiqueWhite2", text="Enter", command=frame5.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(row=6, column=2, pady=0, padx=25)

def food_drink():
    global frame6
    frame6 = Frame(root)
    frame6.grid(row=0, column=0, sticky="NSEW")
    frame6.configure(bg="AntiqueWhite2")



    lblTitle = Label(frame6, fg="black",   bg="AntiqueWhite2", text="Order Food and Drink")
    lblTitle.grid(pady=0, padx=50)

    lblOptions = Label(frame6, fg="black",  bg="AntiqueWhite2", text="Your options:")
    lblOptions.grid(pady=0, padx=0)

    chk_state1 = BooleanVar()
    chk_state1.set(False)
    chk1 = Checkbutton(frame6, fg="black",  bg="AntiqueWhite2", text='Water | $1.00', var=chk_state1) # check box with name of item
    chk1.grid(pady=0, padx=0)

    boxq1 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq1.grid(pady=0, padx=0)

    chk_state2 = BooleanVar()
    chk_state2.set(False)
    chk2 = Checkbutton(frame6,fg="black",  bg="AntiqueWhite2", text='Flavoured Water | $1.50', var=chk_state2) # check box with name of item
    chk2.grid(pady=0, padx=0)

    boxq2 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq2.grid(pady=0, padx=0)

    chk_state3 = BooleanVar()
    chk_state3.set(False)
    chk3 = Checkbutton(frame6, fg="black",  bg="AntiqueWhite2", text='Cola | $4.00', var=chk_state3) # check box with name of item
    chk3.grid(pady=0, padx=0)

    boxq3 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq3.grid(pady=0, padx=0)

    chk_state4 = BooleanVar()
    chk_state4.set(False)
    chk4 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Lemonade | $3.50', var=chk_state4) # check box with name of item
    chk4.grid(pady=0, padx=0)

    boxq4 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq4.grid(pady=0, padx=0)

    chk_state5 = BooleanVar()
    chk_state5.set(False)
    chk5 = Checkbutton(frame6, fg="black",  bg="AntiqueWhite2", text='Iced Chocolate | $4.00', var=chk_state5) # check box with name of item
    chk5.grid(pady=0, padx=0)

    boxq5 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq5.grid(pady=0, padx=0)

    chk_state6 = BooleanVar()
    chk_state6.set(False)
    chk6 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Hot Coffee | $4.00', var=chk_state6)# check box with name of item
    chk6.grid(pady=0, padx=0)

    boxq6 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq6.grid(pady=0, padx=0)

    chk_state7 = BooleanVar()
    chk_state7.set(False)
    chk7 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Hot Chocolate | $4.00', var=chk_state7) # check box with name of item
    chk7.grid(pady=0, padx=0)

    boxq7 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq7.grid(pady=0, padx=0)

    lblOptions = Label(frame6, fg="black", bg="AntiqueWhite2", text="Your Options:")
    lblOptions.grid(row=0, column=2, pady=0, padx=0)

    chk_state8 = BooleanVar()
    chk_state8.set(False)
    chk8 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Hotdog | $2.00', var=chk_state8) # check box with name of item
    chk8.grid(row=1, column=2, pady=0, padx=0)

    boxq8 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq8.grid(row=2, column=2, pady=0, padx=0)

    chk_state9 = BooleanVar()
    chk_state9.set(False)
    chk9 = Checkbutton(frame6, fg="black",  bg="AntiqueWhite2", text='Pie | $4.50', var=chk_state9) # check box with name of item
    chk9.grid(row=3, column=2, pady=0, padx=0)

    boxq9 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq9.grid(row=4, column=2, pady=0, padx=0)

    chk_state10 = BooleanVar()
    chk_state10.set(False)
    chk10 = Checkbutton(frame6, fg="black",  bg="AntiqueWhite2", text='Burger | $6.00', var=chk_state10) # check box with name of item
    chk10.grid(row=5, column=2, pady=0, padx=0)

    boxq10 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq10.grid(row=6, column=2, pady=0, padx=0)

    chk_state11 = BooleanVar()
    chk_state11.set(False) 
    chk11 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Pizza | $6.00', var=chk_state11) # check box with name of item
    chk11.grid(row=7, column=2, pady=0, padx=0)

    boxq11 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq11.grid(row=8, column=2, pady=0, padx=0)

    chk_state12 = BooleanVar()
    chk_state12.set(False)
    chk12 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Sandwich | $3.20', var=chk_state12) # check box with name of item
    chk12.grid(row=9, column=2, pady=0, padx=0)

    boxq12 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq12.grid(row=10, column=2, pady=0, padx=0)

    chk_state13 = BooleanVar()
    chk_state13.set(False)
    chk13 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Hot Chips | $4.00', var=chk_state13) # check box with name of item
    chk13.grid(row=11, column=2, pady=0, padx=0)

    boxq13 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq13.grid(row=12, column=2, pady=0, padx=0)

    chk_state14 = BooleanVar()
    chk_state14.set(False)
    chk14 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Onion Rings | $3.00', var=chk_state14) # check box with name of item
    chk14.grid(row=13, column=2, pady=0, padx=0)

    boxq14 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5) # spin box sets quantity of item
    boxq14.grid(row=14, column=2, pady=0, padx=0)

    chk_state15 = BooleanVar()
    chk_state15.set(False)
    chk15 = Checkbutton(frame6, fg="black", bg="AntiqueWhite2", text='Wraps | $4.00', var=chk_state15) # check box with name of item
    chk15.grid(row=15, column=2, pady=0, padx=0) 

    boxq15 = Spinbox(frame6, bg="AntiqueWhite2", fg="black", from_=0, to=100, width=5)# spin box sets quantity of item
    boxq15.grid(row=16, column=2, pady=0, padx=0)

    error_lbl = Label(frame6, bg="AntiqueWhite2", fg="black")
    error_lbl.grid(pady=0, padx=0)

    def order_total_f():
        try:
            price1 = 0
            price2 = 0
            price3 = 0
            price4 = 0# sets the price to 0 dollars 
            price5 = 0
            price6 = 0
            price7 = 0
            price8 = 0
            price9 = 0
            price10 = 0
            price11 = 0
            price12 = 0
            price13 = 0
            price14 = 0
            price15 = 0

            if chk_state1.get() == True:
                price1 = 1.0 * int(boxq1.get())
            if chk_state2.get() == True:
                price2 = 1.50 * int(boxq2.get())
            if chk_state3.get() == True:
                price3 = 4.0 * int(boxq3.get())# if the user sets a checkbox, it sets the above variables with the price multiplied by the quantity in this if statment
            if chk_state4.get() == True:
                price4 = 3.5 * int(boxq4.get())
            if chk_state5.get() == True:
                price5 = 4.0 * int(boxq5.get())
            if chk_state6.get() == True:
                price6 = 4.0 * int(boxq6.get())
            if chk_state7.get() == True:
                price7 = 4.0 * int(boxq7.get())
            if chk_state8.get() == True:
                price8 = 2.0 * int(boxq8.get())
            if chk_state9.get() == True:
                price9 = 4.5 * int(boxq9.get())
            if chk_state10.get() == True:
                price10 = 6.0 * int(boxq10.get())
            if chk_state11.get() == True:
                price11 = 6.0 * int(boxq11.get())
            if chk_state12.get() == True:
                price12 = 3.2 * int(boxq12.get())
            if chk_state13.get() == True:
                price13 = 4.0 * int(boxq13.get())
            if chk_state14.get() == True:
                price14 = 3.0 * int(boxq14.get())
            if chk_state15.get()  == True:
                price15 = 4.0 * int(boxq15.get())

            order_total = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8 + price9 + price10 + price11 + price12 + price13 + price14 + price15

            lblTotalTitle = Label(frame6, fg="black", bg="AntiqueWhite2", text="Your Order Total is($):")
            lblTotalTitle.grid(row=0, column=3, pady=0, padx=0, sticky=NSEW)

            lblTotal = Label(frame6, fg="black", bg="AntiqueWhite2", text=order_total)
            lblTotal.grid(row=1, column=3, pady=0, padx=0, sticky=NSEW)
        except ValueError:
            error_lbl.configure(text="There was an error with\n your quantities, please enter numbers only.")

    order_total_f()

    btnEnter = Button(frame6, fg="black", bg="AntiqueWhite2", text="Calculate Price", command=order_total_f)
    btnEnter.grid(row=2, column=3, pady=0, padx=0)

    lblTotal = Label(frame6, fg="black", bg="AntiqueWhite2", text= "Are you sure you want to Order?")
    lblTotal.grid(row=3, column=3, pady=0, padx=0)

    rad1 = Radiobutton(frame6, fg="black", bg="AntiqueWhite2", text='Yes', value=1)
    rad1.grid(row=4, column=3, pady=0, padx=0)

    rad2 = Radiobutton(frame6, fg="black", bg="AntiqueWhite2", text='No', value=0)
    rad2.grid(row=5, column=3, pady=0, padx=0)


    btnClose = Button(frame6, fg="black", bg="AntiqueWhite2", text="Enter", command=frame6.destroy) # destroys the frame if the user closes the frame
    btnClose.grid(row=6, column=3, pady=0, padx=0)

def exit_p():
    exit()

def check_password(entryUser1, entryPass1, error_label):
    global frame3
    with open("4th_account.txt", "r") as passfile:
        for line in passfile:
            if entryUser1 + entryPass1 == line.strip():
                frame3 = Frame(root)
                frame3.grid(row=0, column=0, sticky="NSEW")
                frame3.configure(bg="AntiqueWhite2")

                emptySpace = Label(frame3, bg="AntiqueWhite2", text="")
                emptySpace.grid(padx=200 ,pady=50)

                btnOrderFood = Button(frame3, fg="black",  bg="AntiqueWhite2", text="Order Food", command=orderfood)
                btnOrderFood.grid(padx=200 ,pady=0)

                btnOrderDrink = Button(frame3, fg="black",  bg="AntiqueWhite2", text="Order Drink", command=order_drink)
                btnOrderDrink.grid(padx=200 ,pady=0)

                btnOrderFoodAndDrink = Button(frame3, fg="black", bg="AntiqueWhite2", text="Order Food and Drink", command=food_drink)
                btnOrderFoodAndDrink.grid(padx=200 ,pady=0)

                btnLogOut = Button(frame3, text="Log Out", fg="black", bg="AntiqueWhite2", command=logout)
                btnLogOut.grid(padx=200 ,pady=0)

                btnExit = Button(frame3, text="Exit", fg="black", bg="AntiqueWhite2", command=exit_p)
                btnExit.grid(padx=200 ,pady=0)
                return True
    error_label.config(text="Username or Password is incorrect!\n Please try again")
    return False

if password_true == "!password_placeholder_text!": #this is the actual main code it decides what function to run depending on the contents of the txt file. If the file has the placeholder text,it will run the first frame otherwise it will run the second frmae
    frames1()
else:
    frames1()

root.mainloop() # ends the main loop
