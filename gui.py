import sys
import customtkinter as ctk
from PIL import Image

# ----------------------------- TKinter Settings -----------------------------#

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title("BookStore")
root.geometry('1200x600')

#logo = ctk.CTkImage(dark_image=Image.open(r'C:\Users\anton\Desktop\standard_test_images\ANTEIKU.jpg'))

def on_close():
    print("Closing application...")
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_close)

search_input = ctk.CTkEntry(root, placeholder_text='Search',
                            justify='center').pack(pady=30)

welcome = ctk.CTkLabel(root, text="Welcome! Today's offers...", 
                       font=("Helvetica", 36, "bold")).pack(padx=200, pady=20)

root.mainloop()
