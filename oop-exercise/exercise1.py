from datetime import datetime, date,timedelta
#Digital library system


class Book:
    def __init__(self,title,author,isbn,status = "available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,value):
        if value == "available" or value == "rented":
            self._status = value
        else:
            raise ValueError("Status Error")

    def __str__(self):
        return f"Book title: {self.title}| Author: {self.author}| ISBN: {self.isbn}| Status: {self.status}."

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', '{self.status}')"

class User:
    def __init__(self,name,surname,id_card):
        self.name = name
        self.surname = surname
        self.id_card = id_card
        self.rent_list = []

    

    def can_rent(self):
        if len(self.rent_list) >= 3:
            return False
        else:
            return True
        
    def __str__(self):
        return f"The User {self.name} {self.surname}| ID {self.id_card} - {self.rent_list}"
    
    def __repr__(self):
        return f"User('{self.name}', '{self.surname}','{self.id_card},'{self.rent_list}')"
    
class Loan:
    def __init__(self,book,user):
        self.book = book
        self.user = user
        self.loan_date = date.today()
        self.due_date = self.loan_date + timedelta(days=14)
    
    def __str__(self):
        return f"Today {self.loan_date}| The current book {self.book.title} loan to {self.user.id_card} for {self.due_date}"
    
    def __repr__(self):
        return f"Loan('{self.loan_date}','{self.book.title}','{self.user.id_card}','{self.due_date}')"


class MaxLoanExceeded(Exception):
    pass

class Library:
    def __init__(self,library):
        self.library = library
        self.catalogue = []
        self.loan_books = []


    def add_book(self,book):
        self.catalogue.append(book)

    def lend_book(self,isbn,user):
       for book in self.catalogue:
           if book.isbn == isbn:
               if book.status == "rented":
                   return f"Errore."
               if user.can_rent() == False:
                   raise MaxLoanExceeded("User cannot loan")
               book.status = "rented"
               loan = Loan(book,user)
               self.loan_books.append(loan)
               user.rent_list.append(loan)
               

    def return_book(self,isbn,user):
        for loan_book in self.loan_books:
            if loan_book.book.isbn == isbn and loan_book.user == user:
                loan_book.book.status = "available"
                self.loan_books.remove(loan_book)
                user.rent_list.remove(loan_book)
                return
    
    def search_book(self,query):
        for book in self.catalogue:
            if book.isbn == query or book.title == query:
                return book
        return None 



if __name__ == "__main__":
    lib = Library("Central Library")
    b1 = Book("Il Nome della Rosa","Eco","978-000-1")
    u1 = User("Andrea","Rossi","T001")
    lib.add_book(b1)
    print(b1)
    lib.lend_book("978-000-1", u1)
    print(b1)
    print(u1)
    lib.return_book("978-000-1",u1)
    print(b1)
    print(u1)









