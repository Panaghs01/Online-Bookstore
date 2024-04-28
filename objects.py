class Book:
    def __init__(self, title, isbn, genre, author, publisher, price):
        self.title = title
        self.isbn = isbn
        self.genre = genre
        self.author = author
        self.publisher = publisher
        self.price = price
        
        
class Stationary:
    def __init__(self, ids, name, category, corporation, price):
        self.id = ids
        self.name = name
        self.category = category
        self.corporation = corporation
        self.price = price
