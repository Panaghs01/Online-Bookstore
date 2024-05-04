# --------------------------------- Libraries --------------------------------#

import os
import sys
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
#import objects.py

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

# ----------------------------------------------------------------------------#

# Top left logo settings.
logo_path = "ANTEIKU.png"
logo = ctk.CTkImage(light_image=Image.open(logo_path), 
                    dark_image=Image.open(logo_path), size=(160, 160))
logo_label = ctk.CTkLabel(root, text="", image=logo).place(x=0, y=0)

# ----------------------------------------------------------------------------#

# Search settings.
def search_books():
    # Get the search query from the search input
    search_query = search_input.get()
    
    messagebox.showinfo("Search Results", f"Searching for: {search_query}")

def open_search_results():
    # Create a new window
    search_window = ctk.CTk()
    search_window.title("Search Results")
    search_window.geometry('400x300')
    
    search_query = search_input.get()
    search_results_label = ctk.CTkLabel(search_window, text=f"Search Results for: {search_query}", 
                                        font=("Helvetica", 16)).pack(pady=20)
    
    search_window.mainloop()

search_input = ctk.CTkEntry(root, placeholder_text='Search',
                            justify='center')
search_input.pack(pady=30)

search_icon_path = "search_icon.png"
search_icon = ctk.CTkImage(light_image=Image.open(search_icon_path), 
                           dark_image=Image.open(search_icon_path), 
                           size=(27, 27))

search_label = ctk.CTkLabel(root, text="", image=search_icon, cursor="hand2")
search_label.place(x=495, y=29)
search_label.bind("<Button-1>", lambda e: search_books())

# ----------------------------------------------------------------------------#

# Front label settings.
welcome_frame = ctk.CTkFrame(root)
welcome_frame.pack(padx=100, pady=20)
welcome = ctk.CTkLabel(welcome_frame, text="Welcome! Today's offers...", 
                       font=("Helvetica", 36, "bold")).pack(padx=200, pady=20)

# ----------------------------------------------------------------------------#

# Contact us settings.
def open_contact_window():
    contact_window = ctk.CTk()
    contact_window.title("Contact Information")
    contact_window.geometry('330x180')
    
    email_label = ctk.CTkLabel(contact_window, text="Email: anteikubookstore@gmail.com", 
                                font=("Helvetica", 16)).pack(pady=20)
    
    telephone_label = ctk.CTkLabel(contact_window, text="Telephone: xx+xxxxxxx", 
                                    font=("Helvetica", 16)).pack(pady=10)
    
    address_label = ctk.CTkLabel(contact_window, text="Address: Lamia, Greece", 
                                  font=("Helvetica", 16)).pack(pady=10)
    contact_window.mainloop()
    
contact_label = ctk.CTkLabel(root, text="Contact us!", font=("Helvetica", 22), 
                             cursor="hand2")
contact_label.place(x=30, y=530)
contact_label.bind("<Button-1>", lambda e: open_contact_window())

# ----------------------------------------------------------------------------#

# Cart button settings.
def open_cart_window():
    cart_window = ctk.CTk()
    cart_window.title("Cart")
    cart_window.geometry('400x400')
    
    items_label = ctk.CTkLabel(cart_window, text="Total Items",
                               font=("Helvetica", 20)).pack(pady=10)
    
    
    # Showing the items bought.
    
    
    def orderComplete():
        
        # Sending the order data to the database.
        
        pass
    
    proceed_button = ctk.CTkButton(cart_window, text="Proceed to Purchase", 
                                   command=orderComplete).place(x=130, y=350)
    
    cart_window.mainloop()

cart_label = ctk.CTkLabel(root, text="Cart", font=("Helvetica", 22), cursor="hand2")
cart_label.place(x=1070, y=30)
cart_label.bind("<Button-1>", lambda e: open_cart_window())

cart_image_path = "cart.png"
cart_image = ctk.CTkImage(light_image=Image.open(cart_image_path), 
                          dark_image=Image.open(cart_image_path), size=(40, 40))
cart_image_label = ctk.CTkLabel(root, text="", image=cart_image)
cart_image_label.place(x=1120, y=25)

# ----------------------------------------------------------------------------#

# User settings. (Log in - Sign up)
def open_profile():
    
    def login():
        # Clearing previous data.
        for widget in user_window.winfo_children():
            widget.destroy()
        
        username_label = ctk.CTkLabel(user_window, text="Username", 
                                      font=("Helvetica", 16)).pack(pady=10)
        username_entry = ctk.CTkEntry(user_window).pack(pady=5)
        
        password_label = ctk.CTkLabel(user_window, text="Password", 
                                      font=("Helvetica", 16)).pack(pady=10)
        password_entry = ctk.CTkEntry(user_window, show="*").pack(pady=5)
        
        login_button = ctk.CTkButton(user_window, text="Login",
                                     command=login_user).pack(pady=10)

    def signup():
        # Clearing previous data.
        for widget in user_window.winfo_children():
            widget.destroy()
        
        username_label = ctk.CTkLabel(user_window, text="Username", 
                                      font=("Helvetica", 16)).pack(pady=5)
        username_entry = ctk.CTkEntry(user_window).pack(pady=5)
        
        password_label = ctk.CTkLabel(user_window, text="Password", 
                                      font=("Helvetica", 16)).pack(pady=5)
        password_entry = ctk.CTkEntry(user_window, show="*").pack(pady=5)
        
        phone_label = ctk.CTkLabel(user_window, text="Phone", 
                                   font=("Helvetica", 16)).pack(pady=5)
        phone_entry = ctk.CTkEntry(user_window).pack(pady=5)
        
        email_label = ctk.CTkLabel(user_window, text="Email", 
                                   font=("Helvetica", 16)).pack(pady=5)
        email_entry = ctk.CTkEntry(user_window).pack(pady=5)
        
        address_label = ctk.CTkLabel(user_window, text="Address", 
                                     font=("Helvetica", 16)).pack(pady=5)
        address_entry = ctk.CTkEntry(user_window).pack(pady=5)
        
        signup_button = ctk.CTkButton(user_window, text="Sign Up", 
                                      command=signup_user).pack(pady=10)

    user_window = ctk.CTk()
    user_window.title("Profile")
    user_window.geometry('400x400')
    
    select_label = ctk.CTkLabel(user_window, text="Please select an option.", 
                                font=("Helvetica", 16)).pack(pady=30)
    
    login_button = ctk.CTkButton(user_window, text="Log In", command=login)
    login_button.pack(pady=10)
    
    signup_button = ctk.CTkButton(user_window, text="Sign Up", command=signup)
    signup_button.pack(pady=10)

    user_window.mainloop()
    
profile_label = ctk.CTkLabel(root, text="User", font=("Helvetica", 22), cursor="hand2")
profile_label.place(x=960, y=30)
profile_label.bind("<Button-1>", lambda e: open_profile())

profile_image_path = "profile.png"
profile_image = ctk.CTkImage(light_image=Image.open(profile_image_path),
                             dark_image=Image.open(profile_image_path), size=(27,27))
profile_image_label = ctk.CTkLabel(root, text="", image=profile_image)
profile_image_label.place(x=1020, y=30)

# ----------------------------------------------------------------------------#

root.mainloop()

# ----------------------------------------------------------------------------#
