class Book:
    def __init__(self, isbn,title,author,total_copies):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__total_copies = total_copies
        self.__copies_available = total_copies

    #Getters Set
    @property
    def isbn(self):
        return self.__isbn
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    @property
    def copies_available(self):
        return self.__copies_available
    @property
    def total_copies(self):
        return self.__total_copies
    #Setters Set
    def title(self,value):
        self.__title = value
    def author(self, value):
        self.__author = value
    #Dunder Methods - Double Underscore
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def __eq__(self, other):
        pass


book = Book("978-1-234", "1984", "George Orwell", 3)