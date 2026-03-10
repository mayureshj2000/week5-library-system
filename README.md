# week5-library-system
A comprehensive library management system built using Object-Oriented Programming principles. This system allows librarians to manage books, members, and borrowing operations efficiently.

 Object‑Oriented Programming (OOP).
It manages books, members, and borrowing/returning operations with JSON persistence and strict input validation.

##Core OOP Design
1. Classes
Book: represents a single book in the library.
Member: represents a library member and their borrowed books.
Library: central manager for collections of books and members.
main.py: user interface (menu) that interacts with Library.
​

2. OOP Concepts Used
Encapsulation: each class manages its own data and behavior.
Composition: Library contains many Book and Member objects; each Member holds a list of borrowed Book objects.
Class & instance variables: e.g., Member.MAX_BORROWED vs instance attributes like member_id, borrowed_books.​

File Structure
You can document it like this:
1. book.py: Book class definition.
2. member.py: Member class definition.
3. library.py: Library class and JSON load/save logic.
4. main.py: menu loop and all input validation.
5. data/*.json: persistent storage for books and members.

##book.py – Book Class
Purpose: represent a single book and handle loan status and overdue logic.
Key attributes:
1. title (str): book title.
2. author (str): book author.
3. isbn (str): unique numeric 11‑digit ID.
4. year (str or None): 4‑digit publication year (optional).
5. available (bool): True if not borrowed.
6. borrowed_by (str or None): member ID who borrowed the book.
7. due_date (str or None): due date in YYYY-MM-DD format.
8. date_added (str): date the book was added.

##member.py – Member Class
Purpose: represent a library member and manage the list of books they have borrowed.
Key attributes:
1. name (str): member name (letters and spaces only).
2. member_id (str): 4‑digit numeric ID.
3. borrowed_books (list[Book]): list of Book instances currently borrowed.
4. join_date (str): date the member was registered.
5. MAX_BORROWED (class variable, int = 5): maximum number of books allowed per member.

##library.py – Library Class
Purpose: central manager that holds all books and members, and exposes operations for the UI.
Key attributes:
1. books (dict[str, Book]): mapping from ISBN → Book.
2. members (dict[str, Member]): mapping from member ID → Member.

##main.py – Menu and Input Validation
Purpose: provide a simple text‑based interface for librarians and enforce strong input validation before calling library methods.

##Global behavior:
All user inputs are validated in the UI layer before reaching core logic, preventing invalid data from being stored.
Edge cases are handled gracefully:
- Borrow with no books in the system.
- Searching with no books.
- Returning when a member has no borrowed books.
- Returning a book that the member hasn’t borrowed.

