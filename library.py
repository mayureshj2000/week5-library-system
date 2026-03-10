import json
import os
from datetime import datetime
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}  # isbn -> Book
        self.members = {}  # member_id -> Member
    
    def add_book(self, book):
        if book.isbn in self.books:
            return False, "Book ISBN already exists"
        self.books[book.isbn] = book
        return True, "Book added"
    
    def register_member(self, member):
        if member.member_id in self.members:
            return False, "Member ID already exists"
        self.members[member.member_id] = member
        return True, "Member registered"
    
    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found"
        if isbn not in self.books:
            return False, "Book not found"
        member = self.members[member_id]
        book = self.books[isbn]
        return member.borrow_book(book)
    
    def return_book(self, member_id, title):
        if member_id not in self.members:
            return False, "Member not found"
        member = self.members[member_id]
        success, msg = member.return_book(title)
        return success, msg
    
    def find_book(self, query):
        results = []
        for book in self.books.values():
            if (query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query == book.isbn):
                results.append(book)
        return results
    
    def stats(self):
        total = len(self.books)
        available = sum(1 for b in self.books.values() if b.available)
        overdue = sum(1 for b in self.books.values() if b.is_overdue())
        return f"Total: {total}, Available: {available}, Overdue: {overdue}"
    
    def save_data(self, books_file='data/books.json', members_file='data/members.json'):
        os.makedirs('data', exist_ok=True)
        with open(books_file, 'w') as f:
            json.dump({isbn: book.to_dict() for isbn, book in self.books.items()}, f)
        with open(members_file, 'w') as f:
            json.dump({mid: member.to_dict() for mid, member in self.members.items()}, f)
        print("Data saved")
    
    def load_data(self, books_file='data/books.json', members_file='data/members.json'):
        if os.path.exists(books_file):
            with open(books_file, 'r') as f:
                book_data = json.load(f)
            for isbn, data in book_data.items():
                self.books[isbn] = Book.from_dict(data)
            print("Books loaded")
        if os.path.exists(members_file):
            with open(members_file, 'r') as f:
                member_data = json.load(f)
            for mid, data in member_data.items():
                self.members[mid] = Member.from_dict(data, self.books)
            print("Members loaded")
    
    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"
