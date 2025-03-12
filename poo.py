class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):

        if self.available:
            self.available = False
            print(f"You have borrowed the book {self.title}")
        else:
            print(f"Sorry, the book {self.title} is not available")
    
    def return_book(self):
        self.available = True
        print(f"You have returned the book {self.title}")

class User:
    def __init__(self,name,userid):
        self.name = name
        self.userid = userid
        self.borrowed_books = []
    
    def borrow_book(self,book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"sorry, the book {book.title} is not available")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"Sorry, you have not borrowed the book {book.title}")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self,book):
        self.books.append(book)
        print(f"The book {book.title} has been added to the library")
    
    def register_user(self,user):
        self.users.append(user)
        print(f"User {user.name} has been registered")
    
    def display_books(self):
        print("Books available in the library")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")


Book1 = Book("The Alchemist","Paulo Coelho")
Book2 = Book("The Da Vinci Code","Dan Brown")
Book3 = Book("The Great Gatsby","F. Scott Fitzgerald")
Book4 = Book("The Kite Runner","Khaled Hosseini")
Book5 = Book("The Catcher in the Rye","J.D. Salinger")

User1 = User("Alice",1)
User2 = User("Bob",2)
User3 = User("Charlie",3)


library = Library()
library.add_book(Book1)
library.add_book(Book2)
library.add_book(Book3)
library.add_book(Book4)
library.add_book(Book5)

library.register_user(User1)
library.register_user(User2)
library.register_user(User3)



