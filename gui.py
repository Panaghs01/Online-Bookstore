# --------------------------------- Libraries --------------------------------#

import re
import os
import sys
import customtkinter as ctk #pip install customtkinter
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow
import database_connector as DB

# ----------------------------- TKinter Settings -----------------------------#

# General settings.
script_dir = os.path.dirname(os.path.abspath(__file__))

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title("BookStore")
root.geometry('1200x600')

def on_close():
    print("Closing application...")
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_close)

#-----------------------------------------------------------------------------#

user_id_label = ctk.CTkLabel(root, text="", font=("Helvetica", 16))
user_id_label.pack()

# ----------------------------------------------------------------------------#

# Top left logo settings.
logo_path = "ANTEIKU.png"
logo = ctk.CTkImage(light_image=Image.open(logo_path), 
                    dark_image=Image.open(logo_path), size=(160, 160))
logo_label = ctk.CTkLabel(root, text="", image=logo).place(x=0, y=0)

# ----------------------------------------------------------------------------#

user_id=None
admin_id=None

cart={}

# Search settings.
def search_books():

    # Search query from the search input.
    search_query = search_input.get()

    # Found is a list that contains all the books.
    found = DB.search_books(search_query)

    # Checking if any books were found.
    if found:

        # Creating a new window to display search results.
        search_window = ctk.CTk()
        search_window.title("Search Results")
        search_window.geometry('1000x600')
        
        # Label to display search query
        search_results_label = ctk.CTkLabel(
            search_window, text=f"Search Results for: {search_query}", 
                                             font=("Helvetica", 16))
        search_results_label.pack(pady=20)

        # Frame to contain search results
        results_frame = ctk.CTkFrame(search_window)
        results_frame.pack(padx=20, pady=10)

        def add_to_cart(isbn, quantity_entry):
            global cart
            book_info = next((book for book in found if book[0] == isbn), None)
            if book_info:
                quantity = int(quantity_entry.get())  # Get the quantity from the entry widget
                if isbn in cart:
                    cart[isbn]['quantity'] += quantity
                else:
                    cart[isbn] = {'info': book_info, 'quantity': quantity}

                result = DB.add_book_to_cart(isbn)

                if result != 1:
                    messagebox.showinfo("Added to Cart", "Item added to cart successfully!")
                else:
                    messagebox.showerror("Out of Stock", "Not enough copies of the book in stock.")

        for book_info in found:
        # Frame for each book entry
            book_frame = ctk.CTkFrame(results_frame)
            book_frame.pack(pady=10, anchor="w")
            
            # Label to display book information
            book_label = ctk.CTkLabel(
                book_frame, text=f"ISBN: {book_info[0]}\n"
                                 f"Title: {book_info[1]}\n"
                                 f"Author: {book_info[2]}\n"
                                 f"Publisher: {book_info[3]}\n"
                                 f"Genre: {book_info[4]}\n"
                                 f"Price: {book_info[5]}\n",
                                       font=("Helvetica", 12), justify="left")
            book_label.pack(pady=5, anchor="w")

            # Entry widget for displaying quantity
            quantity_entry = ctk.CTkEntry(book_frame, placeholder_text="1", justify="center", width=5)
            quantity_entry.insert(0, "1")  # Default quantity is 1
            quantity_entry.pack(side="left", padx=10)
        
            # Buttons for adjusting quantity
            increment_button = ctk.CTkButton(
            book_frame, text="+", command=lambda entry=quantity_entry: increment_quantity(entry))
            increment_button.pack(side="left")
        
            decrement_button = ctk.CTkButton(
                book_frame, text="-", command=lambda entry=quantity_entry: decrement_quantity(entry))
            decrement_button.pack(side="left")
            
            # Creating an Add to Cart button for each book.
            add_to_cart_button = ctk.CTkButton(
                book_frame, text="Add To Cart", 
                command=lambda isbn=book_info[0], entry=quantity_entry: add_to_cart(isbn, entry))
            add_to_cart_button.pack(pady=5, anchor="w")
        
        search_window.mainloop()

     # Book not found message.
    else:
        messagebox.showinfo(
            "Search Results", "No items found matching your search.")

def increment_quantity(entry):
    current_value = int(entry.get())
    entry.delete(0, "end")
    entry.insert(0, str(current_value + 1))
            
def decrement_quantity(entry):
    current_value = int(entry.get())
    if current_value > 1:  # Ensure the quantity doesn't go below 1
        entry.delete(0, "end")
        entry.insert(0, str(current_value - 1))       

search_input = ctk.CTkEntry(root, placeholder_text='Search', justify='center')
search_input.pack(pady=30)

search_icon_path = "search_icon.png"
search_icon = ctk.CTkImage(light_image=Image.open(search_icon_path), 
                           dark_image=Image.open(search_icon_path), 
                           size=(27, 27))

search_label = ctk.CTkLabel(root, text="", image=search_icon, cursor="hand2")
search_label.place(x=480, y=29)
search_label.bind("<Button-1>", lambda e: search_books())

# ----------------------------------------------------------------------------#

# Front label settings.
welcome_frame = ctk.CTkFrame(root)
welcome_frame.pack(padx=100, pady=20)
welcome = ctk.CTkLabel(welcome_frame, text="Welcome! Our latest releases...",
                       font=("Helvetica", 36, "bold")).pack(padx=200, pady=20)

# ----------------------------------------------------------------------------#

# Cart button settings.

user_logged_in = False
admin_logged_in = False

def open_cart_window():

    def increment_cart_quantity(isbn, entry):
        global cart
        current_value = int(entry.get())
        new_value = current_value + 1
        entry.delete(0, "end")
        entry.insert(0, str(new_value))
        cart[isbn]['quantity'] = new_value

    def decrement_cart_quantity(isbn, entry):
        global cart
        current_value = int(entry.get())
        if current_value > 1:
            new_value = current_value - 1
            entry.delete(0, "end")
            entry.insert(0, str(new_value))
            cart[isbn]['quantity'] = new_value

    def remove_from_cart(isbn):
        global cart
        if isbn in cart:
            del cart[isbn]
            cart_window.destroy()  # Close the current cart window
            open_cart_window()  # Open a new cart window 

    cart_window = ctk.CTk()
    cart_window.title("Cart")
    cart_window.geometry('600x400')

    items_label = ctk.CTkLabel(cart_window, text="Total Items",
                               font=("Helvetica", 20)).pack(pady=10)

    # Frame to contain cart items
    cart_frame = ctk.CTkFrame(cart_window)
    cart_frame.pack(padx=20, pady=10)

    for isbn, book_data in cart.items():
        book_info = book_data['info']
        quantity = book_data['quantity']

        book_frame = ctk.CTkFrame(cart_frame)
        book_frame.pack(pady=10, anchor="w")

        book_label = ctk.CTkLabel(
            book_frame, text=f"Title: {book_info[1]}\n"
                            f"Price: {book_info[5]}\n",
                            font=("Helvetica", 12), justify="left")
        book_label.pack(pady=5, anchor="w")

        # Entry widget for displaying quantity
        quantity_entry = ctk.CTkEntry(book_frame, justify="center", width=5)
        quantity_entry.insert(0, str(quantity))  # Set the current quantity
        quantity_entry.pack(side="left", padx=10)

        # Buttons for adjusting quantity
        increment_button = ctk.CTkButton(
            book_frame, text="+", command=lambda isbn=isbn, entry=quantity_entry: increment_cart_quantity(isbn, entry))
        increment_button.pack(side="left")

        decrement_button = ctk.CTkButton(
            book_frame, text="-", command=lambda isbn=isbn, entry=quantity_entry: decrement_cart_quantity(isbn, entry))
        decrement_button.pack(side="left")

        # Button to remove the item from cart
        remove_button = ctk.CTkButton(book_frame, text="Remove",
                                      command=lambda isbn=isbn: remove_from_cart(isbn))
        remove_button.pack(side="left", padx=10)
        
    
    def order_complete():
        global cart, user_logged_in, admin_logged_in
        
        if  admin_logged_in:

            book_dict = {isbn: book_data['quantity'] for isbn, book_data in cart.items()}
            DB.transaction_buy(book_dict)
            messagebox.showinfo(
                "Purchase Complete",
                "Books bought and added to stock successfully!")
                
        else:
            if not user_logged_in:
                messagebox.showinfo(
                    "Authentication Required",
                    "Please log in or sign up before placing an order!")
                open_profile() 
            else:
                print("\n\n\n\n\n\n\n\n\n\n",user_id,"\n\n\n\n\n\n\n\n\n\n")
                # Dictionary with book ISBNs and quantities
                book_dict = {isbn: book_data['quantity'] for isbn, book_data in cart.items()}
                
                # Send the transaction to the database
                DB.transaction_sell(book_dict, user_id)
                    
                cart.clear()
                cart_window.destroy()
                messagebox.showinfo("Order Successful", "Your order was successful!")
            
    # Proceed to Purchase button
    proceed_button = ctk.CTkButton(cart_window, text="Proceed to Purchase",
                                   command=order_complete)
    proceed_button.pack(pady=20, side="bottom")
    
    cart_window.mainloop()


cart_label = ctk.CTkLabel(
                          root, text="Cart", font=("Helvetica", 22),
                              cursor="hand2")
cart_label.place(x=1070, y=30)
cart_label.bind("<Button-1>", lambda e: open_cart_window())

cart_image_path = "cart.png"
cart_image = ctk.CTkImage(light_image=Image.open(cart_image_path), 
                          dark_image=Image.open(
                              cart_image_path), size=(40, 40))
cart_image_label = ctk.CTkLabel(root, text="", image=cart_image)
cart_image_label.place(x=1120, y=25)


# ----------------------------------------------------------------------------#

# Contact us settings.
def open_contact_window():
    contact_window = ctk.CTk()
    contact_window.title("Contact Information")
    contact_window.geometry('330x180')
    
    email_label = ctk.CTkLabel(
                    contact_window, text="Email: anteikubookstore@gmail.com", 
                        font=("Helvetica", 16)).pack(pady=20)
    
    telephone_label = ctk.CTkLabel(
                    contact_window, text="Telephone: xx+xxxxxxx", 
                        font=("Helvetica", 16)).pack(pady=10)
    
    address_label = ctk.CTkLabel(
                    contact_window, text="Address: Lamia, Greece", 
                        font=("Helvetica", 16)).pack(pady=10)
    contact_window.mainloop()
    
contact_label = ctk.CTkLabel(root, text="Contact us!", font=("Helvetica", 22), 
                             cursor="hand2")
contact_label.place(x=30, y=530)
contact_label.bind("<Button-1>", lambda e: open_contact_window())

# ----------------------------------------------------------------------------#

# User settings. (Log in - Sign up)
def open_profile():

    # Validation functions.
    # Phone, Street Number -> Digits.
    # Email -> example@something.something format.
    validate_phone = lambda new_value: new_value.isdigit() or new_value == ""
    validate_street_number = lambda new_value: new_value.isdigit() or new_value == ""
    validate_email = lambda email: re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

    def signup_user():

        # Getting all data from the text boxes.
        name = name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        country = country_entry.get()
        city = city_entry.get()
        street = street_entry.get()
        street_number = street_number_entry.get()
        postal_code = postal_code_entry.get()

        email = email_entry.get()
        if not validate_email(email):
            messagebox.showerror(
                "Invalid Email", "Please enter a valid email address.")
            return

        phone = phone_entry.get()
        if not phone.isdigit():
            messagebox.showerror(
                "Invalid Phone Number",
                "Phone number should contain only numbers.")
            return

        # Data base call. Signing user up.
        result = DB.signup_user(
            name, username, password, country, city, street, street_number,
            postal_code, phone, email)

        if result == "Username already in use":
            messagebox.showerror(
                "Signup Failed", 
                    "Username already in use. Please choose another username.")
        elif result == "Email already in use":
            messagebox.showerror(
                "Signup Failed",
                    "Email already in use. Please choose another email.")
        else:
            messagebox.showinfo(
                "Sign Up Successful", "Your account has been created!")
            back_to_menu()

        back_to_menu()
 
    def login_user():
        global user_logged_in
        #these need to be strings, incase someone has only a numerical password
        #receiving an integer number will make the validation check give 
        #a false negative
        username = username_entry.get()
        password = password_entry.get()

        # Data base call. Checking if credentials are valid.
        user_id = DB.login_user(username, password)

        if user_id == -1:
            messagebox.showerror(
                "Login Failed",
                "Username not found. Please check your username.")
        elif user_id == -2:
            messagebox.showerror(
                "Login Failed", "Invalid password. Please check your password.")
        else:
            messagebox.showinfo(
                "Login Successful", "You have been logged in!")
            username = DB.return_user(user_id)  # Get the username from the user ID
            user_id_label.configure(text=f"{username}", font=("Helvetica", 22))  # Update label
            user_id_label.place(x=860, y=30)
            user_window.destroy()
            user_logged_in = True # User is now logged in

    def login_admin():
        global admin_logged_in

        username = username_entry.get()
        password = password_entry.get()

        # Data base call. Checking if credentials are valid.
        admin_id = DB.login_admin(username, password)

        if admin_id == -1:
            messagebox.showerror(
                "Login Failed",
                "Username not found. Please check your username.")
        elif admin_id == -2:
            messagebox.showerror(
                "Login Failed",
                "Invalid password. Please check your password.")
        else:
            messagebox.showinfo(
                "Login Successful",
                "You have been logged in!")
            username = DB.return_admin(admin_id)  # Get the username from the admin ID
            user_id_label.configure(text=f"{username}", font=("Helvetica", 22))
            user_id_label.place(x=860, y=30)
            show_statistics_button = ctk.CTkButton(root, text="Show Statistics", command=show_statistics)
            show_statistics_button.place(x=1040, y=522)
            user_window.destroy()
            admin_logged_in = True
  
    def show_statistics():
        statistics_window = ctk.CTk()
        statistics_window.title("Statistics")
        statistics_window.geometry('500x400')

        statistics_label = ctk.CTkLabel(
            statistics_window, text="Statistics will be displayed here", font=("Helvetica", 16))
        statistics_label.pack(pady=50)

        statistics_window.mainloop()


    def back_to_menu():

        for widget in user_window.winfo_children():
            widget.destroy()
        build_main_menu()

    def login():

        global username_entry
        global password_entry
        
        # Clearing previous data.
        for widget in user_window.winfo_children():
            widget.destroy()

        username_label = ctk.CTkLabel(user_window, text="Username", 
                                      font=("Helvetica", 16))
        username_label.pack(pady=10)
        username_entry = ctk.CTkEntry(user_window)
        username_entry.pack(pady=5)
        
        password_label = ctk.CTkLabel(user_window, text="Password", 
                                      font=("Helvetica", 16))
        password_label.pack(pady=10)
        password_entry = ctk.CTkEntry(user_window, show="*") # Hiding the password.
        password_entry.pack(pady=5)
        
        login_button = ctk.CTkButton(user_window, text="Login",
                                     command=login_user)
        login_button.pack(pady=10)

        back_button = ctk.CTkButton(
            user_window, text="Back", fg_color="Red", command=back_to_menu)
        back_button.pack(pady=5)

    def admin():

        global username_entry
        global password_entry

        # Clearing previous data.
        for widget in user_window.winfo_children():
            widget.destroy()

        username_label = ctk.CTkLabel(user_window, text="Username",
                                      font=("Helvetica", 16))
        username_label.pack(pady=10)
        username_entry = ctk.CTkEntry(user_window)
        username_entry.pack(pady=5)

        password_label = ctk.CTkLabel(user_window, text="Password",
                                      font=("Helvetica", 16))
        password_label.pack(pady=10)
        password_entry = ctk.CTkEntry(user_window, show="*")  # Hiding the password.
        password_entry.pack(pady=5)

        login_button = ctk.CTkButton(user_window, text="Login",
                                     command=login_admin)
        login_button.pack(pady=10)

        back_button = ctk.CTkButton(
            user_window, text="Back", fg_color="Red", command=back_to_menu)
        back_button.pack(pady=5)

    def signup():

        # Creating global variables for each needed field.
        global name_entry, username_entry, password_entry
        global country_entry, city_entry
        global street_entry, street_number_entry, postal_code_entry
        global phone_entry, email_entry

        # Clearing previous data.
        for widget in user_window.winfo_children():
            widget.destroy()

        # Checking for valid phone number and street number values.
        validation_phone = user_window.register(validate_phone)
        validation_street_number = user_window.register(validate_street_number)

        fields = [
            ("Name", "name_entry"),
            ("Username", "username_entry"),
            ("Password", "password_entry"),
            ("Country", "country_entry"),
            ("City", "city_entry"),
            ("Street", "street_entry"),
            ("Street Number", "street_number_entry"),
            ("Postal Code", "postal_code_entry"),
            ("Phone", "phone_entry"),
            ("Email", "email_entry")
        ]

        # Working with frames to make the fields be left and right.
        left_frame = ctk.CTkFrame(user_window)
        left_frame.pack(side=ctk.LEFT, padx=20, pady=20)

        right_frame = ctk.CTkFrame(user_window)
        right_frame.pack(side=ctk.RIGHT, padx=20, pady=20)

        # Using a for loop instead of manually adding every single field necessary.
        for i, (label_text, entry_var) in enumerate(fields):
            parent_frame = left_frame if i % 2 == 0 else right_frame

            label = ctk.CTkLabel(
                parent_frame, text=label_text, font=("Helvetica", 16))
            label.pack(pady=5)

            if label_text in ["Phone", "Street Number"]:
                entry = ctk.CTkEntry(
                    parent_frame, validate="key",
                    validatecommand=(
                        validation_phone if label_text == "Phone" else validation_street_number, '%P'))
            elif label_text == "Password":
                entry = ctk.CTkEntry(parent_frame, show="*")
            else:
                entry = ctk.CTkEntry(parent_frame)

            entry.pack(pady=5)
            globals()[entry_var] = entry

        signup_button = ctk.CTkButton(
            user_window, text="Sign Up", command=signup_user)
        signup_button.pack(pady=10)

        back_button = ctk.CTkButton(
            user_window, text="Back", fg_color="Red", command=back_to_menu)
        back_button.pack(pady=10)

    def build_main_menu():
        select_label = ctk.CTkLabel(
            user_window, text="Please select an option.",
                font=("Helvetica", 16))
        select_label.pack(pady=30)

        login_button = ctk.CTkButton(
            user_window, text="Log In", command=login)
        login_button.pack(pady=10)

        signup_button = ctk.CTkButton(
            user_window, text="Sign Up", command=signup)
        signup_button.pack(pady=10)

        admin_button = ctk.CTkButton(
            user_window, text="Admin", fg_color="Blue", command=admin)
        admin_button.pack(pady=10)

    user_window = ctk.CTk()
    user_window.title("Profile")
    user_window.geometry('450x450')

    build_main_menu()
    user_window.mainloop()

profile_label = ctk.CTkLabel(
    root, text="User", font=("Helvetica", 22), cursor="hand2")
profile_label.place(x=960, y=30)
profile_label.bind("<Button-1>", lambda e: open_profile())

profile_image_path = "profile.png"
profile_image = ctk.CTkImage(
                light_image=Image.open(profile_image_path),
                    dark_image=Image.open(profile_image_path), size=(27, 27))
profile_image_label = ctk.CTkLabel(root, text="", image=profile_image)
profile_image_label.place(x=1020, y=30)


root.mainloop()

# ----------------------------------------------------------------------------#



# Main Shopping Interface Function
def open_main_shopping_interface():
    # Create a new window for the main shopping interface
    main_window = ctk.CTk()
    main_window.title("Bookstore")
    main_window.geometry('800x600')

    
    welcome_label = ctk.CTkLabel(
        main_window, text="Welcome to Anteiku!", font=("Helvetica", 22))
    welcome_label.pack(pady=20)

    main_window.mainloop()


# ----------------------------------------------------------------------------#


root.mainloop()


# ----------------------------------------------------------------------------#

