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
        return f"{self.title} by {self.author} ({self.copies_available}/{self.total_copies} available) "
    def __repr__(self):
        return f"Book(isbn='{self.isbn})"
    def __eq__(self, other):
        return self.isbn == other.isbn

    def borrow(self):
        if self.copies_available > 0:
            self.__copies_available -= 1
            return True
        else:
            return False
    def return_book(self):
        if self.copies_available < self.total_copies:
            self.__copies_available +=1
            return True
        else:
            return False

    def is_available(self):
        if self.copies_available > 0:
            self.__copies_available -=1
            return True
        else:
            return False

    def to_dict(self):
        pass
    def from_dict(self, data):
        pass


book = Book("978-1-234", "1984", "George Orwell", 3)