class Member:
    def __init__(self,member_id,name,borrow_limit=5):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []
        self.__borrow_limit = borrow_limit

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
