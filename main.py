from library import Library


def display_menu():
    """Display the main menu options"""
    print("\n" + "=" * 50)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1.  Add book")
    print("2.  Remove book")
    print("3.  Search books")
    print("4.  View all books")
    print("5.  View available books")
    print("6.  Register member")
    print("7.  Remove member")
    print("8.  View all members")
    print("9.  Borrow book")
    print("10. Return book")
    print("11. View member's borrowed books")
    print("12. Save and exit")
    print("13. Exit without saving")
    print("=" * 50)


def add_book(library):
    """Add a new book to the library"""
    print("\n--- Add Book ---")
    isbn = input("Enter ISBN: ").strip()
    if not isbn:
        print("✗ ISBN cannot be empty!")
        return

    title = input("Enter title: ").strip()
    if not title:
        print("✗ Title cannot be empty!")
        return

    author = input("Enter author: ").strip()
    if not author:
        print("✗ Author cannot be empty!")
        return

    try:
        copies = int(input("Enter number of copies: "))
        if copies <= 0:
            print("✗ Number of copies must be positive!")
            return
    except ValueError:
        print("✗ Please enter a valid number!")
        return

    result = library.add_book(isbn, title, author, copies)
    if result == True:
        print(f"✓ Book '{title}' added successfully!")
    else:
        print(f"✗ Book with ISBN {isbn} already exists")


def remove_book(library):
    """Remove a book from the library"""
    print("\n--- Remove Book ---")
    isbn = input("Enter ISBN: ").strip()
    if not isbn:
        print("✗ ISBN cannot be empty!")
        return

    book = library.find_book(isbn)
    if not book:
        print(f"✗ Book with ISBN {isbn} not found")
        return

    result = library.remove_book(isbn)
    if result:
        print(f"✓ Book removed successfully!")
    else:
        print(f"✗ Cannot remove book. Some copies are still borrowed.")


def search_books(library):
    """Search for books by title or author"""
    print("\n--- Search Books ---")
    print("1. Search by title")
    print("2. Search by author")
    choice = input("Choose search type: ").strip()

    if choice not in ["1", "2"]:
        print("✗ Invalid choice!")
        return

    keyword = input("Enter search keyword: ").strip()
    if not keyword:
        print("✗ Keyword cannot be empty!")
        return

    if choice == "1":
        results = library.search_by_title(keyword)
    else:
        results = library.search_by_author(keyword)

    if results:
        print(f"\nFound {len(results)} book(s):")
        for book in results:
            print(f"  - {book}")
    else:
        print("✗ No books found matching your search")


def view_all_books(library):
    """Display all books in the library"""
    print("\n--- All Books ---")
    books = library.get_all_books()

    if books:
        print(f"Total books: {len(books)}")
        for book in books:
            print(f"  - {book}")
    else:
        print("No books in the library")


def view_available_books(library):
    """Display all available books"""
    print("\n--- Available Books ---")
    books = library.get_available_books()

    if books:
        print(f"Available books: {len(books)}")
        for book in books:
            print(f"  - {book}")
    else:
        print("No available books at the moment")


def register_member(library):
    """Register a new member"""
    print("\n--- Register Member ---")
    name = input("Enter member name: ").strip()
    if not name:
        print("✗ Name cannot be empty!")
        return

    member_id = library.register_member(name)
    print(f"✓ Member registered successfully!")
    print(f"  Member ID: {member_id}")
    print(f"  Name: {name}")


def remove_member(library):
    """Remove a member from the library"""
    print("\n--- Remove Member ---")
    member_id = input("Enter member ID: ").strip()
    if not member_id:
        print("✗ Member ID cannot be empty!")
        return

    member = library.find_member(member_id)
    if not member:
        print(f"✗ Member with ID {member_id} not found")
        return

    result = library.remove_member(member_id)
    if result:
        print(f"✓ Member removed successfully!")
    else:
        print(f"✗ Cannot remove member. They still have borrowed books.")


def view_all_members(library):
    """Display all registered members"""
    print("\n--- All Members ---")
    members = library.get_all_members()

    if members:
        print(f"Total members: {len(members)}")
        for member in members:
            print(f"  - {member}")
    else:
        print("No members registered")


def borrow_book(library):
    """Process a book borrowing transaction"""
    print("\n--- Borrow Book ---")
    member_id = input("Enter member ID: ").strip()
    if not member_id:
        print("✗ Member ID cannot be empty!")
        return

    isbn = input("Enter ISBN: ").strip()
    if not isbn:
        print("✗ ISBN cannot be empty!")
        return

    # Validate member exists
    member = library.find_member(member_id)
    if not member:
        print(f"✗ Member with ID {member_id} not found")
        return

    # Validate book exists
    book = library.find_book(isbn)
    if not book:
        print(f"✗ Book with ISBN {isbn} not found")
        return

    # Attempt to borrow
    result = library.borrow_book(member_id, isbn)
    if result:
        print(f"✓ Book borrowed successfully!")
        print(f"  {member.name} now has {member.books_borrowed_count}/{member._Member__borrow_limit} books")
    else:
        # Determine why it failed
        if not book.is_available():
            print(f"✗ No copies of '{book.title}' are currently available")
        elif not member.can_borrow():
            print(f"✗ {member.name} has reached the borrowing limit")
        else:
            print(f"✗ Unable to borrow book")


def return_book(library):
    """Process a book return transaction"""
    print("\n--- Return Book ---")
    member_id = input("Enter member ID: ").strip()
    if not member_id:
        print("✗ Member ID cannot be empty!")
        return

    isbn = input("Enter ISBN: ").strip()
    if not isbn:
        print("✗ ISBN cannot be empty!")
        return

    # Validate member exists
    member = library.find_member(member_id)
    if not member:
        print(f"✗ Member with ID {member_id} not found")
        return

    # Validate book exists
    book = library.find_book(isbn)
    if not book:
        print(f"✗ Book with ISBN {isbn} not found")
        return

    # Attempt to return
    result = library.return_book(member_id, isbn)
    if result:
        print(f"✓ Book returned successfully!")
        print(f"  {member.name} now has {member.books_borrowed_count}/{member._Member__borrow_limit} books")
    else:
        print(f"✗ {member.name} does not have this book borrowed")


def view_member_books(library):
    """View all books borrowed by a member"""
    print("\n--- Member's Borrowed Books ---")
    member_id = input("Enter member ID: ").strip()
    if not member_id:
        print("✗ Member ID cannot be empty!")
        return

    member = library.find_member(member_id)
    if not member:
        print(f"✗ Member with ID {member_id} not found")
        return

    books = library.get_member_books(member_id)

    print(f"\n{member.name}'s borrowed books:")
    if books:
        for book in books:
            print(f"  - {book}")
    else:
        print("  No books currently borrowed")


def main():
    """Main program loop"""
    library = Library()

    # Try to load existing library data
    print("Loading library data...")
    try:
        library.load_from_file("library_data.json")
        print(f"✓ Library data loaded successfully!")
        print(f"  {library}")
    except FileNotFoundError:
        print("No existing data found. Starting with empty library.")
    except Exception as e:
        print(f"Error loading data: {e}")
        print("Starting with empty library.")

    # Main program loop
    while True:
        display_menu()
        choice = input("\nChoose option (1-13): ").strip()

        if choice == "1":
            add_book(library)

        elif choice == "2":
            remove_book(library)

        elif choice == "3":
            search_books(library)

        elif choice == "4":
            view_all_books(library)

        elif choice == "5":
            view_available_books(library)

        elif choice == "6":
            register_member(library)

        elif choice == "7":
            remove_member(library)

        elif choice == "8":
            view_all_members(library)

        elif choice == "9":
            borrow_book(library)

        elif choice == "10":
            return_book(library)

        elif choice == "11":
            view_member_books(library)

        elif choice == "12":
            # Save and exit
            try:
                library.save_to_file("library_data.json")
                print("\n✓ Library data saved successfully!")
                print("Goodbye!")
                break
            except Exception as e:
                print(f"\n✗ Error saving data: {e}")
                confirm = input("Exit anyway? (y/n): ").strip().lower()
                if confirm == 'y':
                    print("Goodbye!")
                    break

        elif choice == "13":
            # Exit without saving
            confirm = input("\nAre you sure you want to exit without saving? (y/n): ").strip().lower()
            if confirm == 'y':
                print("Goodbye!")
                break

        else:
            print("✗ Invalid option. Please choose 1-13.")


if __name__ == "__main__":
    main()