# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:04:37 2024

@author: panos
"""

import mysql.connector as sql


connect = sql.connect(user = "root", host = "localhost", database = "bookstore")

cursor = connect.cursor()
cursor.execute("desc books")
table = cursor.fetchall()

print('\n Table Description:') 
for attr in table: 
    print(attr) 

query = "INSERT INTO books (ISBN, title, author, publisher, genre) VALUES (121212121212,'test','teste','testee','testeee')"
cursor.execute(query)
connect.commit()

connect.close()