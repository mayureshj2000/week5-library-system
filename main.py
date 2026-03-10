from datetime import datetime, timedelta
from book import Book
from member import Member
from library import Library

def main():
    lib = Library()
    lib.load_data()
    
    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Stats")
        print("0. Save & Exit")
        choice = input("Choose: ").strip()
        
        if choice == '1':
            # Title: letters and spaces only
            while True:
                title = input("Title: ").strip()
                if title.replace(" ", "").isalpha():
                    break
                print("Title must contain letters and spaces only.")

             # Author: letters and spaces only
            while True:
                author = input("Author: ").strip()
                if author.replace(" ", "").isalpha():
                    break
                print("Author must contain letters and spaces only.")

            # ISBN: digits only, 11 digits
            while True:
                isbn = input("ISBN (11 digits): ").strip()
                if isbn.isdigit() and len(isbn) == 11:
                    break
                print("ISBN must be a numeric value with exactly 11 digits.")
            # Year: optional, but if given must be 4 digits
            while True:
                year = input("Year (4 digits, optional): ").strip()
                if year == "":
                    year_val = None
                    break
                if year.isdigit() and len(year) == 4:
                    year_val = year
                    break
                print("Year must be a 4‑digit number (e.g. 2024), or leave blank.")
            
            book = Book(title, author, isbn, year_val)
            success, msg = lib.add_book(book)
            print(msg)

        elif choice == '2':
            # Name: letters and spaces only
            while True:
                name = input("Name: ").strip()
                if name.replace(" ", "").isalpha():
                    break
                print("Name must contain letters and spaces only.")

            # Member ID: digits only, 4 digits
            while True:
                mid = input("Member ID (4 digits): ").strip()
                if mid.isdigit() and len(mid) == 4:
                    break
                print("Member ID must be numeric with exactly 4 digits.")

            member = Member(name, mid)
            success, msg = lib.register_member(member)
            print(msg)

        elif choice == '3':
            if not lib.books:
                print("No books available in the library.")
                continue

            # Member ID: digits only, 4 digits
            while True:
                mid = input("Member ID (4 digits): ").strip()
                if mid.isdigit() and len(mid) == 4:
                    break
                print("Member ID must be numeric with exactly 4 digits.")

            # ISBN: digits only, 11 digits
            while True:
                isbn = input("ISBN (11 digits): ").strip()
                if isbn.isdigit() and len(isbn) == 11:
                    break
                print("ISBN must be numeric with exactly 11 digits.")

            success, msg = lib.borrow_book(mid, isbn)
            print(msg)

        elif choice == '4':
            while True:
                mid = input("Member ID (4 digits): ").strip()
                if mid.isdigit() and len(mid) == 4:
                    break
                print("Member ID must be numeric with exactly 4 digits.")

            # Book title: letters and spaces only
            while True:
                title = input("Book title: ").strip()
                if title.replace(" ", "").isalpha():
                    break
                print("Title must contain letters and spaces only.")

            success, msg = lib.return_book(mid, title)
            print(msg)

        elif choice == '5':
            if not lib.books:
                print("No books available in the library to search.")
                continue

            # Search query: letters and spaces only (for title/author)
            while True:
                query = input("Search (title/author): ").strip()
                if query.replace(" ", "").isalpha():
                    break
                print("Search term must contain letters and spaces only.")

            books = lib.find_book(query)
            if books:
                for b in books:
                    print(b)
            else:
                print("No matches")

        elif choice == '6':
            print(lib.stats())
        elif choice == '0':
            lib.save_data()
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()