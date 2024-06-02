"""

Implemented functions: 
    searching books
    signup and login for user
    login for admin
    add to cart 
    make a sale
    make a purchase

feel free to fuck around with what each function returns, to fit whatever 

the giu.py code requires

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


def signup_user(name, username, password, country, city, street, street_number,
                postal_code, phone, email):
    #this is not yet called in gui.py, need to implement more gui elements to get
    #all the necessary values for a new user
    
    cursor.execute("SELECT username FROM customers")
    usernames = cursor.fetchall() 
    cursor.execute("SELECT email FROM customers")
    emails = cursor.fetchall()
    if username in usernames: return "Username already in use"
    if email in emails: return "Email already in use"
    #dont know if multiline string breaks the sql query
    #only time will tell
    cursor.execute(
        f"""INSERT INTO customers (name, username, password, country, city, 
                street, street_num, postal_code, phone, email) 
        VALUES ({name}, {username}, {password}, {country}, {city}, {street}, 
                {street_number}, {postal_code}, {phone}, {email})""")
    cursor.commit()
    
   
def login_user(username, password):
    #this is also not yet called in gui.py, im letting it up to you to decide 
    #when and how to call it 
    
    cursor.execute("SELECT username FROM customers")
    usernames = cursor.fetchall()
    if username not in usernames:
        return -1 #Invalid username error
    else:
        cursor.execute(
            f"SELECT password FROM customers WHERE username={username}")
        passwords = cursor.fetchall()
        if password not in passwords: return -2 #Invalid password error
        else: 
            cursor.execute(
                f"""SELECT id FROM customers 
                WHERE username={username} AND password={password}""")
            user_id = cursor.fetchall() #this might return a tuple
            return user_id #login sucessful, return users id
        

def login_admin(username, password):
    cursor.execute("SELECT username FROM admins")
    usernames = cursor.fetchall()
    if username not in usernames:
        return -1 #Invalid username error
    else:
        cursor.execute(
            f"SELECT password FROM admins WHERE username={username}")
        passwords = cursor.fetchall()
        if password not in passwords: return -2 #Invalid password error
        else:
            cursor.execute(
                f"""SELECT id FROM admins 
                WHERE username={username} AND password={password}""")
            admin_id = cursor.fetchall()
            return admin_id #login sucessful
        

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
