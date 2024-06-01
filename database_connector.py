"""

Implemented functions: 
    searching books
    signup and login for user

feel free to fuck around with what each function returns, to fit whatever 

the giu.py code requires

e.g. you could make search books return only the name or id of the book
or tell me to change it however you like 

-xrhstos

"""

import mysql.connector as sql

database = sql.connect(user = "root", host = "localhost",
                       database = "bookstore")

cursor = database.cursor()

#returns books that are like user_input, takes optional argument columns(tuple)
#which is default as * and returns everything for that book
def search_books(user_input, columns="*"): 
    cursor.execute(
        f"SELECT {columns} FROM books WHERE title LIKE '%{user_input}%'")
    result = cursor.fetchall() 
    #result is a list of tuples that contains the SQL query result
    return result


#this is not yet called in gui.py, need to implement more gui elements to get
#all the necessary values for a new user
def signup_user(name, username, password, country, city, street, street_number,
                postal_code, phone, email):
    cursor.execute(f"SELECT username FROM customers")
    usernames = cursor.fetchall() 
    cursor.execute(f"SELECT email FROM customers")
    emails = cursor.fetchall()
    if username in usernames: return "Username already in use"
    if email in emails: return "Email already in use"
    #ugly fucking line of code, tell me if u know how to make it not be so long
    cursor.execute(
        f"INSERT INTO customers (name, username, password, country, city, street, street_num, postal_code, phone, email) VALUES ({name}, {username}, {password}, {country}, {city}, {street}, {street_number}, {postal_code}, {phone}, {email})")
    
#this is also not yet called in gui.py, im letting it up to you to decide 
#when and how to call it    
def login_user(username, password):
    cursor.execute("SELECT username FROM customers")
    usernames = cursor.fetchall()
    if username not in usernames:
        return 1 #Invalid username error
    else:
        cursor.execute(
            f"SELECT password FROM customers WHERE username={username}")
        passwords = cursor.fetchall()
        if password not in passwords: return 2 #Invalid password error
        else: return 0 #login sucessful
        

def login_admin(username, password):
    cursor.execute("SELECT username FROM admins")
    usernames = cursor.fetchall()
    if username not in usernames:
        return 1 #Invalid username error
    else:
        cursor.execute(
            f"SELECT password FROM admins WHERE username={username}")
        passwords = cursor.fetchall()
        if password not in passwords: return 2 #Invalid password error
        else: return 0 #login sucessful
        
#this function takes book_isbn and optionally a value that is default to 1
#and returns if book can be added to cart or if it is out of stock
#THIS HAS NOT BEEN TESTED YET, if statement might need minor adjustments
def add_book_to_cart(isbn,quantity=1):
    cursor.execute(f"SELECT quantity FROM inventory WHERE book_ISBN={isbn}")
    inventory = cursor.fetchall()
    if inventory[0][0] - quantity >= 0: return 0 #Success
    else: return 1 #Not enough copies of the book in stock







