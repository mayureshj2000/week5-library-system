from datetime import datetime
from book import Book

class Member:
    MAX_BORROWED = 5
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # list of Book objects
        self.join_date = datetime.now().strftime('%Y-%m-%d')
    
    def borrow_book(self, book: Book) -> tuple[bool, str]:
        if len(self.borrowed_books) >= Member.MAX_BORROWED:
            return False, f"Max {Member.MAX_BORROWED} books limit"
        if not book.available:
            return False, "Book not available"
        success, msg = book.check_out(self.member_id)
        if success:
            self.borrowed_books.append(book)
        return success, msg
    
    def return_book(self, title: str) -> tuple[bool, str]:
        # NEW: handle case when no books borrowed
        if not self.borrowed_books:
            return False, "No books borrowed."
        
        for i, book in enumerate(self.borrowed_books):
            if book.title == title:
                book.return_book()
                del self.borrowed_books[i]
                return True, "Book returned successfully."
        
        return False, "Book not found in your borrowed list."
    
    def list_borrowed(self):
        if not self.borrowed_books:
            return "No borrowed books"
        return "\n".join(str(book) for book in self.borrowed_books)
    
    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": [b.isbn for b in self.borrowed_books],
            "join_date": self.join_date,
        }
    
    @classmethod
    def from_dict(cls, data, book_dict):
        member = cls(data["name"], data["member_id"])
        member.join_date = data.get("join_date", datetime.now().strftime("%Y-%m-%d"))
        for isbn in data.get("borrowed_books", []):
            if isbn in book_dict:
                member.borrowed_books.append(book_dict[isbn])
        return member
    
    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"