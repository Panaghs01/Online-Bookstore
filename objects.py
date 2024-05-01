# ---------------------------------- Objects ---------------------------------#

# Possible genre: 
#    Literature, Manga, Poems

class Book:
    def __init__(self, title, isbn, genre, author, publisher, price, cover):
        self.title = title
        self.isbn = isbn
        self.genre = genre
        self.author = author
        self.publisher = publisher
        self.price = price
        self.cover = cover
        
class Stationary:
    def __init__(self, ids, name, category, corporation, price):
        self.id = ids
        self.name = name
        self.category = category
        self.corporation = corporation
        self.price = price
        
# ----------------------------- Creating Objects -----------------------------#

kafka_on_the_shore = Book("Kafka on the Shore", "01", "Literature", "Murakami Haruki", "Vintage Books", "12.99", "kafka_on_the_shore.jpg")
oneq84_1_and_2 = Book("1Q84 Books 1 and 2", "02", "Literature", "Murakami Haruki", "Vintage Books", "13.99", "1q84_1.jpg")
oneq84_3 = Book("1Q84 Book 3", "03", "Literature", "Murakami Haruki", "Vintage Books", "13.99", "1q84_3.jpg")
kokoro = Book("Kokoro", "04", "Literature", "Natsume Soseki", "Vintage Books", "11.99", "kokoro.jpg")
chuuya = Book("Nakahara Chuuya Poems", "05", "Poems", "Nakahara Chuuya", "Gracewing", "16.99", "chuuya_poems.jpg")
jp_poems = Book("100 poems, 100 authors", "06", "Poems", "-", "Penguin Classics", "12.99", "poems.jpg")
pun_1 = Book("Goodnight Punpun Volume 1", "07", "Manga", "Asano Inio", "VIZ Media LLC", "16.99", "pun_1.jpg")
pun_2 = Book("Goodnight Punpun Volume 2", "08", "Manga", "Asano Inio", "VIZ Media LLC", "16.99", "pun_2.jpg")
pun_3 = Book("Goodnight Punpun Volume 3", "09", "Manga", "Asano Inio", "VIZ Media LLC", "16.99", "pun_3.jpg")
stone_ocean_1 = Book("JOJO Stone Ocean Volume 1", "10", "Manga", "Araki Hirohiko", "VIZ Media LLC", "12.99", "stone_ocean_1")
stone_ocean_2 = Book("JOJO Stone Ocean Volume 2", "11", "Manga", "Araki Hirohiko", "VIZ Media LLC", "12.99", "stone_ocean_2")
stone_ocean_2 = Book("JOJO Stone Ocean Volume 3", "12", "Manga", "Araki Hirohiko", "VIZ Media LLC", "12.99", "stone_ocean_3")
snow_country = Book("Snow Country", "13", "Literature", "Kawabata Yasunari", "Knopf Doubleday Publishing Group", "9.99", "snow_country.jpg")
