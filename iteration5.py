#George Robinson
#Iteration 5
#BDSC Cafe

from tkinter import * # imports the TKinter code
from PIL import Image, ImageTk # enters a specific tkinter code where you can insert images into the program

root = Tk()  # sets the root as Tk()
root.title("Botany Downs Secondary College Cafe")  # top of program title 
root.geometry("850x650") # sets the size of the widnow
root.configure(bg="AntiqueWhite2") # sets thebackground colour 
unpw = {} 
with open("4th_account.txt") as file: # opens the 4th account text file
    password_true = file.readline().strip()  # strips spaces from the password

def logout(): 
    frame6.destroy()    # log out function closes the frame 6 frame and runs the frame 1 function/frame
    frames1()

def frames1():
    global frame1
    frame1 = Frame(root)
    frame1.grid(row=0, column=0, sticky="nesw")
    frame1.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame1, text="")
    emptySpace.grid(pady=60, padx=365) 
    emptySpace.configure(bg="AntiqueWhite2") #empty space for aesthetics

    img = Image.open("bdsc.png") # loads the bdsc logo image
    img = img.resize((120, 120)) # sets the appropriate size
    img1 = ImageTk.PhotoImage(img)
    la_bel = Label(frame1, image=img1) # puts the image into a label so that it can be easily configurde 
    la_bel.image = img1
    la_bel.grid(pady=0, padx=365) # changing position of image label 
    la_bel.configure(bg="AntiqueWhite2")

    lblPass = Label(frame1, text="BDSC Cafe")
    lblPass.grid(pady=0, padx=365)
    lblPass.configure(fg="brown4", bg="AntiqueWhite2", font=("TkDefaultFont", 18, "bold")) # changing boldness and colour of text 

    Button(frame1, fg="black", text="Create Account", width=12,command=create_account).grid(pady=0, padx=225) # button to create account and runs create_account function/frame
    Button(frame1, text="Log In", fg="black", width=12, command=frames2).grid(pady=0, padx=365) # Log in button runs frames2 function/frame

def create_account():
    global frame10
    frame10 = Frame(root)
    frame10.grid(row=0, column=0, sticky="nsew")
    frame10.configure(bg="AntiqueWhite2")

    img = Image.open("bdsc.png") # loads the bdsc logo image
    img = img.resize((100, 100))  # sets the appropriate size
    img1 = ImageTk.PhotoImage(img)
    la_bel = Label(frame10, image=img1)
    la_bel.image = img1# puts the image into a label so that it can be easily configurde 
    la_bel.grid(pady=0, padx=225) # changing position of image label 
    la_bel.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame10, text="")
    emptySpace.grid(pady=15, padx=300) # empty space 
    emptySpace.configure(bg="AntiqueWhite2")

    lblThank = Label(frame10, text="Thanks for creating an account for the BDSC Cafe!")
    lblThank.grid(pady=0, padx=0)
    lblThank.configure(fg="brown4", bg="AntiqueWhite2", font=("TkDefaultFont", 14, "bold")) # sets colour and boldness of text 

    lblUser = Label(frame10, bg="AntiqueWhite2", fg="black", text="\n \nUsing the following Entry Box, \ncan you please enter your new useranme:")
    lblUser.grid(pady=0, padx=0)

    entryUser = Entry(frame10, fg="black")
    entryUser.grid(pady=0, padx=0)

    lblPass = Label(frame10, bg="AntiqueWhite2", fg="black", text="Using the following Entry Box, \ncan you please enter your new password:")
    lblPass.grid(pady=0, padx=0)

    entryPass = Entry(frame10, fg="black", show="*") # hides what user is entering by showing* 
    entryPass.grid(pady=0, padx=0)

    lblEmpty = Label(frame10, bg="AntiqueWhite2", fg="black", text="")
    lblEmpty.grid(pady=0, padx=0)

    lblAge = Label(frame10, bg="AntiqueWhite2", fg="black", text="Please enter your age:")
    lblAge.grid(pady=0, padx=0)

    boxAge = Spinbox(frame10, fg="black", from_=0, to=130, width=5) # Spinbox asks user for their age, must be 13-18
    boxAge.grid(pady=0, padx=0)

    age_error_label = Label(frame10, bg="AntiqueWhite2", fg="red")
    age_error_label.grid(pady=0, padx=0)
    
    def on_create_account():
        age_v = int(boxAge.get())

        if age_v <= 12 or age_v >= 19:
            age_error_label.config(text="To create this account, you need to\n be 13-18 years old (High School Age)") # of not high school age, this messsage will appear 
        else:
            set_password(entryUser.get(), entryPass.get()) # if in range the set_password function will happen

        return

    btnLogin = Button(frame10, bg="AntiqueWhite2", fg="black", text="Create Account", command=on_create_account) # button to create account 
    btnLogin.grid(pady=0, padx=0)

    btnBack = Button(frame10, bg="AntiqueWhite2", fg="black", text="Back", command=frames1) # button to log in
    btnBack.grid(pady=0, padx=0)

def set_password(entryUser, entryPass):
    with open("4th_account.txt", "a") as file:
        file.write(entryUser + entryPass + "\n")
    options_menu()



def frames2(): # This frame asks for the password, so any returning users will have to enter their password before entering and viewing their acount naems and passwords
    global frame2
    frame2 = Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew")
    frame2.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame2, text="")
    emptySpace.grid(row=0, column=0, pady=20, padx=300) # empty space
    emptySpace.configure(bg="AntiqueWhite2")

    #this is the image used in the above two functions, see coments if needed
    img = Image.open("bdsc.png")
    img = img.resize((100, 100))
    img1 = ImageTk.PhotoImage(img)
    la_bel = Label(frame2, image=img1)
    la_bel.image = img1
    la_bel.grid(row=1, column=0, pady=0, padx=300)
    la_bel.configure(bg="AntiqueWhite2")

    lblUser = Label(frame2, bg="AntiqueWhite2", fg="black", text="Please enter your Username below:")
    lblUser.grid(row=2, column=0, pady=0, padx=300)

    entryUser1 = Entry(frame2, fg="black") # changes the viewable characters as a dot to hide what they are typing
    entryUser1.grid(row=3, column=0, pady=0, padx=300)

    lblPass = Label(frame2, bg="AntiqueWhite2", fg="black", text="Please enter your Password below:")
    lblPass.grid(row=4, column=0, pady=0, padx=300)

    entryPass1 = Entry(frame2, fg="black", show="*") # changes the viewable characters as a dot to hide what they are typing
    entryPass1.grid(row=5, column=0, pady=0, padx=300)

    btnLogin = Button(frame2, bg="AntiqueWhite2", fg="black", text="Log In", command=lambda: check_password(entryUser1.get(), entryPass1.get(), error_label)) # log in button 
    btnLogin.grid(row=6, column=0, pady=35, padx=300)

    error_label = Label(frame2, fg="red", bg="AntiqueWhite2")
    error_label.grid(row=7, column=0, pady=0, padx=300)

    btnBack = Button(frame2, bg="AntiqueWhite2", fg="black", text="Back to Home", command=frames1)  # home button 
    btnBack.grid(row=8, column=0, pady=0, padx=300)



def orderfood():
    global framet
    framet = Frame(root)
    framet.grid(row=0, column=0, sticky="nsew")
    framet.configure(bg="AntiqueWhite2")
    images = ["wraps.png", "sandwich.png", "pizza.png", "pie.png", "onionrings.png", "hotdog.png", "chips.png", "burger.png"] # stores the images into a list 
    description = ["Soft Taco filled with\nVegetables and Sauce.", "Healthy Sandwich with\nHam Filling.", "Delicious Cheesy topping\nwith Pepperoni.", "Mince and Cheese pie \nwith delicious Pastry.", "Crispy Onion Rings.", "Delicious American\nStyle Hot dog.", "Crispy Potato Chips.", "Amazing Beef Burger."] # stores the descriptions into the list 
    prices = [4, 3.20, 6, 4.50, 3, 2, 4, 6] # prices in the list 
    pics = [] #sets the pics list as nothing
    spin_boxes = [] # sets spin boxes as nothing 
    selected_items = []  # New list to store selected item descriptions
    def get_selected_items(spin_boxes):
        selected_items = []
        for i, spin_box in enumerate(spin_boxes): # every spinbox has a numerical value associated with it and is put into the two above lists 
            quantity = int(spin_box.get())
            if quantity > 0:
                selected_items.append(description[i]) # with that number, it associates the appropriate spin box with the corresponding descroption then stores that in the selected items list
        return selected_items

    for i, image_path in enumerate(images):
        photo = Image.open(image_path) # for the amount of times in image path it prints each phto 
        photo1 = ImageTk.PhotoImage(photo)
        pics.append(photo1) # puts the photo into the empty pic list 
        row = i // 4 # allows the description, spinbox, and image to be in the correct positions
        column = i % 4# allows the description, spinbox, and image to be in the correct positions
        l = Label(framet, image=pics[i], bg="AntiqueWhite2")
        l.grid(row=row*3, column=column, padx=0, pady=0) # uses the above code to put the images in the correct position
        l.image = photo1
        des = Label(framet, text=description[i], wraplength=150, justify="center") # descripion is the amount of times this code has been run and that number is used to the corresponding item in the list
        des.grid(row=row*3+1, column=column, padx=0, pady=0)
        number = Spinbox(framet, from_=0, to=100)
        number.grid(row=row*3+2, column=column, padx=0, pady=0) # spinbox is also using the above code so the description, spinbox, and image to be in the correct positions
        spin_boxes.append(number) 

    global total_label
    total_label = Label(framet, text="Total Price: $0.00") # the defult text is zero dollars but this is updated in later code
    total_label.grid(row=9, columnspan=4, padx=0, pady=25)

    def update_total():
        total = 0
        selected_items.clear()  # Clear the selected items list
        for i, spin_box in enumerate(spin_boxes): # for every time in spin boxes
            try:
                quantity = int(spin_box.get())
                total += quantity * prices[i] # timeses the corresponding quantity with price
                if quantity > 0:
                    selected_items.append(description[i])  # Add selected item's description
                    print(f"Selected: {description[i]}") # uses dictionary to write each description in the print stament so it can be viewed in the terminal
            except ValueError: 
                total_label.config(text="Please enter a valid number")
                return
        total_label.config(text=f"Total Price: ${total:.2f}") # configures the $0.00 to the true price

    
    for spin_box in spin_boxes:
        spin_box.config(command=update_total)

    btnEnter = Button(framet, bg="AntiqueWhite2", text="Next", width=15, command=lambda: order_history_d(total_label.cget("text"), get_selected_items(spin_boxes))) # runs the confirmation code
    btnEnter.grid(row=10, column=2, padx=0, pady=50)
    btnBack = Button(framet, bg="AntiqueWhite2", text="Back", width=15, command=framet.destroy) # destroys the frmae to go back
    btnBack.grid(row=10, column=1, padx=0, pady=50)


def back_func_f():
    framet1.destroy() # When the function is called, it will destroy the frame and run the options menu 
    options_menu()

def order_history_f(total, selected_items):
    global framet1
    framet1 = Frame(root)
    framet1.grid(row=0, column=0, sticky="nsew")
    framet1.configure(bg="AntiqueWhite2")
    Label(framet1, bg="AntiqueWhite2", text="Your Order summary:").grid(padx=0, pady=0)

    order_summary_label = Label(framet1, bg="AntiqueWhite2", justify="left") # this will be configured to show the items the user has selected
    order_summary_label.grid(padx=0, pady=0)
    
    # Display the selected items' descriptions
    order_summary_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(selected_items)]) # prints each description so the user can see what they are ordering
    order_summary_label.configure(text=order_summary_text, justify=LEFT)
    
    Label(framet1, bg="AntiqueWhite2", text=total).grid(padx=0, pady=0) # prints order totla

    appearb = Button(framet1, bg="AntiqueWhite2", text="Complete Order", command=back_func_f) # when this button is pressed, the back_func function is called 
    appearb.grid(padx=0, pady=0)






    




def order_drink():
    global framed
    framed = Frame(root)
    framed.grid(row=0, column=0, sticky="nsew")
    framed.configure(bg="AntiqueWhite2")
    images = ["water.png", "fwater.png", "cola.png", "lemonade.png", "colddrink.png", "hotdrink.png", "hotdrink2.png"]  # stores the images into a list 
    description = ["Fresh Ice Cold Water", "Flavoured Healthy Water", "Your favorite cola", "Refreshing Lemonade", "Iced Chocolate", "Hot Refreshing coffee", "Hot Refreshing Chocolate"]# stores the descriptions into the list 
    prices = [1, 1.50, 4, 3.50, 4, 4, 4]# prices in the list 
    pics = [] #sets the pics list as nothing
    spin_boxes = []# sets spin boxes as nothing 
    selected_items = []  # List to store selected item descriptions

    def get_selected_items(spin_boxes):
        selected_items = []
        for i, spin_box in enumerate(spin_boxes):  # every spinbox has a numerical value associated with it and is put into the two above lists 
            quantity = int(spin_box.get())
            if quantity > 0:
                selected_items.append(description[i]) # with that number, it associates the appropriate spin box with the corresponding descroption then stores that in the selected items list
        return selected_items

    for i, image_path in enumerate(images):
        photo = Image.open(image_path) # for the amount of times in image path it prints each phto
        photo1 = ImageTk.PhotoImage(photo)
        pics.append(photo1) # puts the photo into the empty pic list 
        row = i // 4 # allows the description, spinbox, and image to be in the correct positions
        column = i % 4 # allows the description, spinbox, and image to be in the correct positions
        l = Label(framed, image=pics[i], bg="AntiqueWhite2")
        l.grid(row=row*3, column=column, padx=0, pady=0)# uses the above code to put the images in the correct position
        l.image = photo1
        des = Label(framed, text=description[i], wraplength=150, justify="center") #descripion is the amount of times this code has been run and that number is used to the corresponding item in the list
        des.grid(row=row*3+1, column=column, padx=0, pady=0)
        number = Spinbox(framed, from_=0, to=100)
        number.grid(row=row*3+2, column=column, padx=0, pady=0)# spinbox is also using the above code so the description, spinbox, and image to be in the correct positions
        spin_boxes.append(number)

    global total_label
    total_label = Label(framed, text="Total Price: $0.00") # the defult text is zero dollars but this is updated in later code
    total_label.grid(row=10, columnspan=4)

    def update_total():
        total = 0
        selected_items.clear()  # Clear the selected items list
        for i, spin_box in enumerate(spin_boxes): # for every time in spin boxes
            quantity = int(spin_box.get())
            if quantity > 0:
                total += quantity * prices[i]  # timeses the corresponding quantity with price
                selected_items.append(description[i])  # Add the selected item description
        total_label.config(text=f"Total Price: ${total:.2f}")

    for spin_box in spin_boxes:
        spin_box.config(command=update_total)

    btnEnter = Button(framed, bg="AntiqueWhite2", text="Next", width=15, command=lambda: order_history_f(total_label.cget("text"), get_selected_items(spin_boxes)))
    btnEnter.grid(row=9, column=2, padx=0, pady=50)
    btnBack = Button(framed, bg="AntiqueWhite2", text="Back", width=15, command=framed.destroy)
    btnBack.grid(row=9, column=1, padx=0, pady=50)

def back_func_d():  #When the function is called, it will destroy the frame and run the options menu 
    framed1.destroy()
    options_menu()


def order_history_d(total, selected_items):
    global framed1
    framed1 = Frame(root)
    framed1.grid(row=0, column=0, sticky="nsew")
    framed1.configure(bg="AntiqueWhite2")
    Label(framed1, bg="AntiqueWhite2", text="Your Order summary:").grid(padx=0, pady=0)

    order_summary_label = Label(framed1, bg="AntiqueWhite2", justify="left") # this will be configured to show the items the user has selected
    order_summary_label.grid(padx=0, pady=0)
    
    # Display the selected items' descriptions
    order_summary_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(selected_items)]) # prints each description so the user can see what they are ordering
    order_summary_label.configure(text=order_summary_text, justify=LEFT)
    
    Label(framed1, bg="AntiqueWhite2", text=total).grid(padx=0, pady=0) # prints order totla

    appearb = Button(framed1, bg="AntiqueWhite2", text="Complete Order", command=back_func_d) # when this button is pressed, the back_func function is called 
    appearb.grid(padx=0, pady=0)






def exit_p(): # exit function runs exit code to stop app
    exit()

def options_menu(): # options menu displays option to user
    global frame6
    frame6 = Frame(root)
    frame6.grid(row=0, column=0, sticky="NSEW")
    frame6.configure(bg="AntiqueWhite2")

    emptySpace = Label(frame6, bg="AntiqueWhite2", text="")
    emptySpace.grid(row=0, column=0, padx=315 ,pady=80)
    
    lblT = Label(frame6, text="BDSC Cafe Options:")
    lblT.grid(row=1, column=0, padx=315 ,pady=7)
    lblT.configure(fg="brown4", bg="AntiqueWhite2", font=("TkDefaultFont", 15, "bold")) # changes colour and boldness

    btnOrderFood = Button(frame6, fg="black",  bg="AntiqueWhite2", width=20 ,text="Order Food", command=orderfood) # button
    btnOrderFood.grid(row=2, column=0, padx=315 ,pady=7)

    btnOrderDrink = Button(frame6, fg="black",  bg="AntiqueWhite2", width=20 , text="Order Drink", command=order_drink) # button
    btnOrderDrink.grid(row=3, column=0, padx=315 ,pady=7)

    btnLogOut = Button(frame6, text="Log Out", fg="black", width=20 , bg="AntiqueWhite2", command=logout) # button
    btnLogOut.grid(row=4, column=0, padx=315 ,pady=7)

    btnExit = Button(frame6, text="Exit", fg="black", width=20 , bg="AntiqueWhite2", command=exit_p) # button
    btnExit.grid(row=5, column=0, padx=315 ,pady=7)




def check_password(entryUser1, entryPass1, error_label): # checks the password with the external file

    with open("4th_account.txt", "r") as passfile:
        for line in passfile:
            if entryUser1 + entryPass1 == line.strip():
                options_menu()
                return True
    error_label.config(text="Username or Password is incorrect!\n Please try again")
    return False

if password_true == "!password_placeholder_text!": #this is the actual main code it decides what function to run depending on the contents of the txt file. If the file has the placeholder text,it will run the first frame otherwise it will run the second frmae
    frames1()
else:
    frames1()

root.mainloop() # ends the main loop