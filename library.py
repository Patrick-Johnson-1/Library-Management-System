from book import Book
from member import Member
import json

class Library:
    def __init__(self):
        self.__books = {}
        self.__members = {}
        self.__next_member_id = 1
    def add_book(self,isbn,title,author,copies):
        if isbn in self.__books:
            return "Book Already exists"
        else:
            book = Book(isbn,title,author,copies)
            self.__books[isbn] = book
            return True
    def remove_book(self, isbn):
        if isbn in self.__books:
            book = self.__books[isbn]
            if book.copies_available == book.total_copies:
                self.__books.pop(isbn)
                return True
            else:
                return False
        else:
            return False

    def find_book(self, isbn):
         if isbn in self.__books:
             return self.__books[isbn]
         else:
             return None

    def search_by_title(self, keyword):
        results = []
        for book in self.__books.values():
            if keyword.lower() in book.title.lower():
                results.append(book)
        return results

    def search_by_author(self, keyword):
        return [
            book for book in self.__books.values()
            if keyword.lower() in book.author.lower()

        ]

    def get_available_books(self):
        results = []
        for book in self.__books.values():
            if book.is_available() :
                results.append(book)
        return results

    def register_member(self, name):
        member_id = f"M{self.__next_member_id:03d}"
        self.__next_member_id += 1

        member = Member(member_id, name)
        self.__members[member_id] = member
        return member_id

    def remove_member(self, member_id):
        member = self.__members.get(member_id)
        if not member:
            return False
        if member.books_borrowed_count > 0:
            return False

        self.__members.pop(member_id)
        return True

    def get_all_books(self):
        return list(self.__books.values())

    def find_member(self, member_id):
        if member_id in self.__members:
            return self.__members[member_id]
        else:
            return None

    def get_all_members(self):
        return list(self.__members.values())
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False
        if not book.is_available():
            return False
        if not member.can_borrow():
            return False

        member.borrow_book(isbn)
        book.borrow()

        return True

    def return_book(self,member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return False
        if member.has_book(isbn):
            book.return_book()
            member.return_book(isbn)
            return True
        else:
            return False

    def get_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            return []

        # Get ISBNs member has borrowed
        isbn_list = member.borrowed_books

        # Convert ISBNs to Book objects
        books = []
        for isbn in isbn_list:
            book = self.find_book(isbn)
            if book:
                books.append(book)

        return books

    def __len__(self):
        return len(self.__books)

    def __str__(self):
        return  f"Library: {len(self.__books)} books, {len(self.__members)} members"

    def save_to_file(self,filename):
        data = {
            "next_member_id": self.__next_member_id,
            "books": [],
            "members": []
        }
        for book in self.__books.values():
            data["books"].append(book.to_dict())

        for member in self.__members.values():
            data["members"].append(member.to_dict())
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self,filename):
        with open(filename, 'r') as f:
            data = json.load(f)

        # Step 2: Load books
        for book_data in data["books"]:
            book = Book.from_dict(book_data)
            self.__books[book.isbn] = book

        # Step 3: Load members
        for member_data in data["members"]:
            member = Member.from_dict(member_data)
            self.__members[member.member_id] = member

        # Step 4: Restore next_member_id
        self.__next_member_id = data["next_member_id"]


