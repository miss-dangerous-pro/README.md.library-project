from datetime import date

# Base Person class and derived classes Member and Librarian
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Member(Person):
    def __init__(self, name, address, membership):
        super().__init__(name, address)
        self.membership = membership  
        self.borrowed_novels = []  

    def borrow_novel(self, library, novel_title):
        if library.lend_novel(novel_title, self):
            self.borrowed_novels.append(novel_title)
            print(f"{self.name} borrowed '{novel_title}'")
        else:
            print(f"'{novel_title}' is not available or checked out.")

    def return_novel(self, library, novel_title):
        if novel_title in self.borrowed_novels:
            library.receive_novel(novel_title, self)
            self.borrowed_novels.remove(novel_title)
            print(f"{self.name} returned '{novel_title}'")

class Librarian(Person):
    def __init__(self, name, address):
        super().__init__(name, address)

    def add_novel(self, library, novel):
        library.add_novel(novel)
        print(f"Librarian {self.name} added '{novel.title}' to the library.")

# Membership Class to handle member subscription details
class Membership:
    def __init__(self, membership_type):
        self.membership_type = membership_type
        self.start_date = date.today()
        self.end_date = self.start_date.replace(year=self.start_date.year + 1)

    def is_active(self):
        return date.today() <= self.end_date

# Base Item class and derived Novel class
class Item:
    def __init__(self, title, isbn, copies=1):
        self.title = title
        self.isbn = isbn
        self.copies = copies  

class Author:
    def __init__(self, name, biography=""):
        self.name = name
        self.biography = biography

class Novel(Item):
    def __init__(self, title, author, genre, isbn, copies=1):
        super().__init__(title, isbn, copies)
        self.author = author  
        self.genre = genre  

    def __str__(self):
        return f"'{self.title}' by {self.author.name} (Genre: {self.genre}, ISBN: {self.isbn})"

# Library class that contains and manages novels
class Library:
    def __init__(self, name):
        self.name = name
        self.novels = {}
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} added to the library.")

    def add_novel(self, novel):
        if novel.title in self.novels:
            self.novels[novel.title].copies += novel.copies
        else:
            self.novels[novel.title] = novel

    def lend_novel(self, title, member):
        if title in self.novels and self.novels[title].copies > 0:
            self.novels[title].copies -= 1
            return True
        return False

    def receive_novel(self, title, member):
        if title in self.novels:
            self.novels[title].copies += 1

    def list_available_novels(self):
        print("\nAvailable novels in the library:")
        for title, novel in self.novels.items():
            print(f"{novel} - Copies available: {novel.copies}")

# Creating library, members, librarian, and novels
library = Library("Novel Library")

# Librarian and Members creation
librarian = Librarian("Mr mazzu", "100 Library Ave")
member1 = Member("vusqa", "123 Elm St", Membership("Gold"))
member2 = Member("destroyer", "456 Oak St", Membership("Silver"))

# Adding members to the library
library.add_member(member1)
library.add_member(member2)

# Creating and adding novels to the library
novel1 = Novel("Pride and Prejudice", Author("Jane Austen"), "First Impressions", "9780141439518", copies=2)
novel2 = Novel("1984", Author("George Orwell"), "Dystopian", "9780451524935", copies=3)
novel3 = Novel("Moby-Dick", Author("Herman Melville"), "Adventure", "9781503280786", copies=1)

# Librarian adds novels to the library
librarian.add_novel(library, novel1)
librarian.add_novel(library, novel2)
librarian.add_novel(library, novel3)

# Listing available novels
library.list_available_novels()

# Member borrows a novel
member1.borrow_novel(library, "1984")

# Listing available novels after borrowing
library.list_available_novels()

# Member returns a novel
member1.return_novel(library, "1984")

# Listing available novels after returning
library.list_available_novels()
