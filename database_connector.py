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
    passwords = cursor.fetchone()
    
    if not passwords:
        return -1  #Invalid username

    if password not in passwords:
        return -2  #Invalid password

    cursor.execute("SELECT id FROM customers WHERE username = %s AND password = %s", (username, password))
    user_id = cursor.fetchone()

    return user_id[0]  #Login successful, returning the user ID.


# Same exact process as the login_user, though this time we use the admins table.
def login_admin(username, password):
    
    cursor.execute("SELECT password FROM admins WHERE username = %s", (username,))
    passwords = cursor.fetchone()

    if not passwords:
        return -1 #Invalid username

    if password not in passwords:
        return -2 #Invalid password
    
    
    cursor.execute("SELECT id FROM admins WHERE username = %s AND password = %s", (username, password))
    admin_id = cursor.fetchone()

    return admin_id[0]


def add_book_to_cart(isbn,quantity=1):
    #this function takes book_isbn and optionally a value that is default to 1
    #and returns if book can be added to cart or if it is out of stock
    
    cursor.execute(
        f"SELECT stock FROM books WHERE ISBN='{isbn}'")
    inventory = cursor.fetchone()
    if inventory[0] - quantity >= 0: return isbn,quantity 
    #Success, return the isbn and the quantity requested
    else: return 1 #Not enough copies of the book in stock, therefore return 1
    

def transaction_sell(book_dict,customer_id):    
    #this function takes a dictionary of {book_isbn:quantity} format 
    #and the customer_id as arguments
    #then makes a transaction
    #it is to be called after all validity checks have been made 
    #and it is to commit a new sale to the 
    
    for key in book_dict.keys():
        cursor.execute(
            f"""INSERT INTO sells (customer_id, book_ISBN, quantity) 
            VALUES ('{customer_id}', '{key}', '{book_dict[key]}')""")
        database.commit()
        cursor.execute(
            f"SELECT stock FROM books WHERE ISBN='{key}'")
        quantity = cursor.fetchone()
        new_quantity=quantity[0]-book_dict[key]
        cursor.execute(
            f"""UPDATE books SET stock = {new_quantity} 
            WHERE ISBN = '{key}'""")
        database.commit()


def transaction_buy(book_dict):
    #this function takes a dictionary of {book_isbn:quantity} format 
    #as an argument
    #then makes a transaction
    #it is to be called to commit a new sale to the database 

    for key in book_dict.keys():
        cursor.execute(
            f"""INSERT INTO buys (book_ISBN, quantity) 
            VALUES ('{key}', '{book_dict[key]}')""")
        database.commit()
        cursor.execute(
            f"SELECT stock FROM books WHERE ISBN='{key}'")
        quantity = cursor.fetchone()
        new_quantity=quantity[0]+book_dict[key]
        cursor.execute(
            f"""UPDATE books SET stock = '{new_quantity}' 
            WHERE ISBN = '{key}'""")
        database.commit()


def customer_transactions(user_id):
    transactions=[]

    cursor.execute("SELECT book_ISBN FROM sells WHERE customer_id=%s", (user_id,))
    result = cursor.fetchall()

    if result:
        transactions.append([isbn[0] for isbn in result])

    return transactions

    '''
    GOING TO REVERT WHEN TRANSACTION DATE IS ADDED
    
    #cursor.execute("SELECT DISTINCT date FROM sells WHERE customer_id=%s", (user_id,))
    dates = cursor.fetchall()

    for adate in date:
        cursor.execute("SELECT book_ISBN FROM sells WHERE date=? AND customer_id=%s", (adate[0], user_id))
        transaction = cursor.fetchall()
        transactions.append((adate[0], [isbn[0] for isbn in transaction]))

    return transaction
    '''

def return_transactions():
    transactions=[]
    cursor.execute("SELECT date FROM sells GROUP BY(date)")
    dates = cursor.fetchall()
    cursor.execute("SELECT customer_id FROM sells GROUP BY(customer_id)")
    customers = cursor.fetchall()
    for date in dates:
        for customer in customers:
            cursor.execute(
                f"""SELECT book_ISBN FROM sells 
                WHERE (date='{date[0]}' AND customer_id='{customer[0]}')""")
            transaction = cursor.fetchall()
            for i in range(len(transaction)):
                if transaction[i][0]:
                    transactions.append(transaction[i][0])
    return transactions


def return_user(customer):
    cursor.execute(
        f"SELECT username FROM customers WHERE ID = '{customer}'")
    customer_id = cursor.fetchone()
    return customer_id[0]


def return_admin(admin):
    cursor.execute(
        f"SELECT username FROM admins WHERE ID = '{admin}'")
    admin_id = cursor.fetchone()
    return admin_id[0]


def get_book_details(isbn):
    cursor.execute("SELECT * FROM books WHERE ISBN = %s", (isbn,))
    book_details = cursor.fetchone()
    return book_details

def get_latest_books():
    query = "SELECT * FROM books ORDER BY date DESC LIMIT 3"
    cursor.execute(query)
    latest_books = cursor.fetchall()
    return latest_books

# Might use it somewhere in the future modcheck
def validate_username(username):
    cursor.execute(
        f"SELECT * FROM customers WHERE username = '{username}'")
    a = cursor.fetchone()
    if a: return True
    return False