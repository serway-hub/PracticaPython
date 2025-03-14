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



class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"


persona1= Persona("Alice",25)
persona2= Persona("Bob",30)


print(persona1.saludar())
print(persona2.saludar())


#paradigmas de programacion
#POO
# ENCAPSULAMIENTO

import random

class CuentaBancaria:
    def __init__(self,titular,cuenta,saldo):
        self,titular = titular
        self.cuenta = cuenta
        self.__saldo = saldo
        self.cuentas =[]
    
    def crear_cuenta(self,titular,cuenta):
        self.titular = titular
        self.cuenta = cuenta

        if cuenta:
            self.cuenta = random.randint(1000,9999)
            self.cuentas.append({
            "titular":self.titular,
            "cuenta":self.cuenta
            })
            if self.cuenta in self.cuentas:
                print(f"Hola {self.titular}, ya tienes una cuenta con el numero {self.cuenta}")
            else:
                print(f"Se ha creado la cuenta {self.cuenta} a nombre de {self.titular}")
            
        else:
            print("Digito una opcion invalida vuelva a intentarlo")
    
    def despositar(self,cantidad):
        self.__saldo += cantidad
        
        print(f"Se han depositado {cantidad} a la cuenta {self.cuenta}")
    
    def retirar(self,cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -=cantidad
            print(f"Se han retirado {cantidad} de la cuenta {self.cuenta}")




       


        print(f"Se ha creado la cuenta {self.cuenta} a nombre de {self.titular}")
    

