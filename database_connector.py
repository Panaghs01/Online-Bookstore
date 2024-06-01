import mysql.connector as sql

database = sql.connect(user = "root", host = "localhost", database = "bookstore")

cursor = database.cursor()

#returns books that are like user_input, takes optional argument columns(tuple)
#which is default as * and returns everything for that book
def search_books(user_input, columns="*"): 
    cursor.execute(f"SELECT {columns} FROM books WHERE title LIKE '%{user_input}%'")
    result = cursor.fetchall() 
    #result is a list of tuples that contains the SQL query result
    return result

def signup_user(name, username, password, country, city, street, street_number,
                postal_code, phone, email):
    cursor.execute(f"SELECT username FROM customers")
    usernames = cursor.fetchall() 
    cursor.execute(f"SELECT email FROM customers")
    emails = cursor.fetchall()
    if username in usernames: return "Username already in use"
    if email in emails: return "Email already in use"
    cursor.execute(f"INSERT INTO customers (name, username, password, country, city, street, street_num, postal_code, phone, email) VALUES ({name}, {username}, {password}, {country}, {city}, {street}, {street_number}, {postal_code}, {phone}, {email})")
    