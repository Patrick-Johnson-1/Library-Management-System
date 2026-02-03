class Book:
    def __init__(self, isbn,title,author,total_copies):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__total_copies = total_copies

book = Book("978-1-234", "1984", "George Orwell", 3)