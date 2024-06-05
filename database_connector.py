"""

Implemented functions: 
    searching books
    signup and login for user
    login for admin
    add to cart 
    make a sale
    make a purchase

feel free to fuck around with what each function returns, to fit whatever 

the gui.py code requires

e.g. you could make search books return only the name or id of the book
or tell me to change it however you like 

-xrhstos

"""

import mysql.connector as sql #pip install mysql-connector

database = sql.connect(user = "root", host = "localhost",
                       database = "bookstore")
cursor = database.cursor()


#returns books that are like user_input, takes optional argument columns(tuple)
#which is default as * and returns everything for that book
def search_books(user_input, columns="*"): 
    cursor.execute(
        f"SELECT {columns} FROM books WHERE title LIKE '%{user_input}%'")
    #this isnt great, for it is not sql injection protected
    result = cursor.fetchall() 
    #result is a list of tuples that contains the SQL query result
    return result


# Takes every field of the sign up boxes, checks if the username or email is in use
# and inserts the fields into the database. (Turned into %s)
def signup_user(name, username, password, country, city, street, street_number,
                postal_code, phone, email):

    cursor.execute("SELECT username FROM customers WHERE username = %s", (username,))
    existing_username = cursor.fetchone()
    if existing_username: # Username already in use.
        return "Username already in use!"

    cursor.execute("SELECT email FROM customers WHERE email = %s", (email,))
    existing_email = cursor.fetchone()
    if existing_email: # Email already in use.
        return "Email already in use!"

    # Adding data into the database.
    cursor.execute(
        """INSERT INTO customers (name, username, password, country, city, 
        street, street_num, postal_code, phone, email) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (name, username, password, country, city, street, street_number, postal_code, phone, email)
    )

    database.commit()


# Checks if the username and password combination is valid. If yes, the user ID is returned.
def login_user(username, password):

    cursor.execute("SELECT password FROM customers WHERE username = %s", (username,))
    stored_password = cursor.fetchone()
    if not stored_password:
        return -1  # Invalid username.

    stored_password = stored_password[0]
    if stored_password != password:
        return -2  # Invalid password.

    cursor.execute("SELECT id FROM customers WHERE username = %s AND password = %s", (username, password))
    user_id = cursor.fetchone()

    return user_id  # Login successful, returning the user ID.


# Same exact process as the login_user, though this time we use the admins table.
def login_admin(username, password):
    cursor.execute("SELECT password FROM admins WHERE username = %s", (username,))
    admin_password = cursor.fetchone()

    if admin_password:
        # Password has position 0 in the tupple.
        admin_password = admin_password[0]

        if admin_password == password:
            cursor.execute("SELECT id FROM admins WHERE username = %s AND password = %s", (username, password))
            admin_id = cursor.fetchone()

            if admin_id:
                return admin_id[0]  # Login successful, returning the admin ID.
            else:
                return -3  # Authentication failed.
        else:
            return -2  # Invalid password.
    else:
        return -1  # Invalid username.


def add_book_to_cart(isbn,quantity=1):
    #this function takes book_isbn and optionally a value that is default to 1
    #and returns if book can be added to cart or if it is out of stock
    #THIS HAS NOT BEEN TESTED YET, if statement might need minor adjustments
    
    cursor.execute(
        f"SELECT quantity FROM inventory WHERE book_ISBN={isbn}")
    inventory = cursor.fetchall()
    if inventory[0] - quantity >= 0: return isbn,quantity 
    #Success, return the isbn and the quantity requested
    else: return 1 #Not enough copies of the book in stock, therefore return 1
    

def transaction_sell(book_dict,customer_id):    
    #this function takes a dictionary of {book_isbn:quantity} format 
    #and the customer_id as arguments
    #then makes a transaction
    #it is to be called after all validity checks have been made 
    #and it is to commit a new sale to the 
    
    for key in book_dict:
        cursor.execute(
            f"""INSERT INTO sells (customer_id, book_ISBN, quantity) 
            VALUES ({customer_id}, {key}, {book_dict[key]})""")
        cursor.commit()
        cursor.execute(
            f"SELECT quantity FROM inventory WHERE book_ISBN={key}")
        quantity = cursor.fetchall()
        new_quantity=quantity[0]-book_dict[key]
        cursor.execute(
            f"""UPDATE inventory SET quantity = {new_quantity} 
            WHERE book_ISBN = {key})""")
        cursor.commit()
       
def transaction_buy(book_dict,supplier_id):
    #this function takes a dictionary of {book_isbn:quantity} format 
    #and the supplier_id as arguments
    #then makes a transaction
    #it is to be called to commit a new sale to the database 
    
    for key in book_dict:
        cursor.execute(
            f"""INSERT INTO buys (supplier_id, book_ISBN, quantity) 
            VALUES ({supplier_id}, {key}, {book_dict[key]})""")
        cursor.commit()
        cursor.execute(
            f"SELECT quantity FROM inventory WHERE book_ISBN={key}")
        quantity = cursor.fetchall()
        new_quantity=quantity[0]+book_dict[key]
        cursor.execute(
            f"""UPDATE inventory SET quantity = {new_quantity} 
            WHERE book_ISBN = {key})""")
        cursor.commit()
