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
    @title.setter
    def title(self,value):
        self.__title = value
    @author.setter
    def author(self, value):
        self.__author = value

    #Dunder Methods - Double Underscore
    def __str__(self):
        return f"{self.title} by {self.author} ({self.copies_available}/{self.total_copies} available) "
    def __repr__(self):
        return f"Book(isbn='{self.isbn}', title='{self.title}')"
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
        return self.copies_available > 0

    def to_dict(self):
        return {
            "isbn": self.__isbn,
            "title": self.__title,
            "author": self.__author,
            "copies_available": self.__copies_available,
            "total_copies": self.__total_copies
        }
    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["isbn"],
            data["title"],
            data["author"],
            data["total_copies"]
        )
        book._Book__copies_available = data["copies_available"]
        return book

book = Book("978-1-234", "1984", "George Orwell", 3)