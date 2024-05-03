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

# Top left logo settings.
logo_path = "ANTEIKU.png"
logo = ctk.CTkImage(light_image=Image.open(logo_path), 
                    dark_image=Image.open(logo_path), size=(160, 160))
logo_label = ctk.CTkLabel(root, text="", image=logo).place(x=0, y=0)

# Search and label settings.
search_input = ctk.CTkEntry(root, placeholder_text='Search',
                            justify='center').pack(pady=30)

search_icon_path = "search_icon.png"
search_icon = ctk.CTkImage(light_image=Image.open(search_icon_path), 
                           dark_image=Image.open(search_icon_path), size=(30, 30))
search_label = ctk.CTkLabel(root, text="", image=search_icon).place(x=495, y=28)

welcome_frame = ctk.CTkFrame(root)
welcome_frame.pack(padx=100, pady=20)
welcome = ctk.CTkLabel(welcome_frame, text="Welcome! Today's offers...", 
                       font=("Helvetica", 36, "bold")).pack(padx=200, pady=20)

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
    
contact_label = ctk.CTkLabel(root, text="Contact us!", font=("Helvetica", 22), cursor="hand2")
contact_label.place(x=30, y=530)
contact_label.bind("<Button-1>", lambda e: open_contact_window())

# Cart button settings.
def open_cart_window():
    cart_window = ctk.CTk()
    cart_window.title("Cart")
    cart_window.mainloop()

cart_label = ctk.CTkLabel(root, text="Cart", font=("Helvetica", 22), cursor="hand2")
cart_label.place(x=1070, y=30)
cart_label.bind("<Button-1>", lambda e: open_cart_window())

# Cart image settings.
cart_image_path = "cart.png"
cart_image = ctk.CTkImage(light_image=Image.open(cart_image_path), 
                          dark_image=Image.open(cart_image_path), size=(40, 40))
cart_image_label = ctk.CTkLabel(root, text="", image=cart_image)
cart_image_label.place(x=1120, y=25)

root.mainloop()
