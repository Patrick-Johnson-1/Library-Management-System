class Member:
    def __init__(self,member_id,name,borrow_limit=5):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []
        self.__borrow_limit = borrow_limit
    def __str__(self):
        count = self.books_borrowed_count
        limit = self.__borrow_limit
        return f"{self.name} (ID: {self.member_id}) - {count}/{limit} books borrowed"
    def __repr__(self):
        return f"Member(id='{self.member_id}', name='{self.name}')"
    def __eq__(self, other):
        return self.member_id == other.member_id
    @property
    def member_id(self):
        return self.__member_id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value
    @property
    def borrowed_books(self):
        return self.__borrowed_books.copy()
    @property
    def books_borrowed_count(self):
        return len(self.__borrowed_books)

    def borrow_book(self, isbn):
        if self.books_borrowed_count < self.__borrow_limit:
            self.__borrowed_books.append(isbn)
            return True
        else:
            return False

    def can_borrow(self):
        return  self.books_borrowed_count < self.__borrow_limit
    def return_book(self,isbn):
        if isbn in self.__borrowed_books:
            self.__borrowed_books.remove(isbn)
            return True
        else:
            return False
    def has_book(self,isbn):
        return isbn in self.__borrowed_books