# --------------------------------- Libraries --------------------------------#

import os
import sys
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

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
logo_label = ctk.CTkLabel(root, text="", image=logo)
logo_label.place(x=10, y=0)

# Label and search settings.
search_input = ctk.CTkEntry(root, placeholder_text='Search',
                            justify='center').pack(pady=30)

# Contact us settings.
def open_contact_window():
    contact_window = ctk.CTk()
    contact_window.title("Contact Information")
    contact_window.geometry('330x180')
    
    email_label = ctk.CTkLabel(contact_window, text="Email: anteikubookstore@gmail.com", 
                                font=("Helvetica", 16)).pack(pady=20)
    
    telephone_label = ctk.CTkLabel(contact_window, text="Telephone: xx+xxxxxxx", 
                                    font=("Helvetica", 16)).pack(pady=10)
    
    address_label = ctk.CTkLabel(contact_window, text="Address: Lamia, Greece (unfort)", 
                                  font=("Helvetica", 16)).pack(pady=10)
    contact_window.mainloop()
    
contact_label = ctk.CTkLabel(root, text="Contact us!", font=("Helvetica", 22), cursor="hand2")
contact_label.place(x=400, y=30)
contact_label.bind("<Button-1>", lambda e: open_contact_window())

# Offer settings.
welcome_frame = ctk.CTkFrame(root)
welcome_frame.pack(padx=100, pady=20)
welcome = ctk.CTkLabel(welcome_frame, text="Welcome! Today's offers...", 
                       font=("Helvetica", 36, "bold")).pack(padx=200, pady=20)

root.mainloop()
