class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lent_books = {}

    def updateBookList(self):
        self.booklist = [book for book in self.booklist if book not in self.lent_books]

    def displayBooks(self):
        print(f"Available books are: {self.booklist}")
        for book, borrower in self.lent_books.items():
            print(f"{book} is lent out to {borrower}")

    def lendBooks(self):
        bookName = input("Which book do you want to lend? ").capitalize()
        if bookName in self.booklist:
            if bookName not in self.lent_books:
                borrower = input("Enter your Name: ")
                self.lent_books[bookName] = borrower
                print("The book has been issued to you.")
            else:
                print("The book is already lent out.")
        else:
            print("The book is not present in the library.")
        self.updateBookList()

    def addBook(self):
        print("Enter the book name below. You can add only one book at a time.")
        while(True):                                                                    
            bookname = input("Enter the name of the book you want to donate : ").capitalize()
            print(f"Thank you for your contribution to the library. Your book: '{bookname}' has been successfully added to our library.")
            userinfo = int(input("Do you want to add another book?\n1: yes, 2: No\n"))
            if userinfo != 1:
                print("See you soon...")
                break
        
    def returnBooks(self):
        bookName = input("Enter the name of the book you want to return: ").capitalize()
        if bookName in self.lent_books:
            self.lent_books.pop(bookName)
            print("The book has been returned successfully.")
        else:
            print("This book is either not lent out or doesn't belong to this library")

myLibrary = Library(["To Kill a Mockingbird","1984","Pride and Prejudice","The Great Gatsby","The Catcher in the Rye","The Hobbit","Fahrenheit 451","Brave New World","Animal Farm","The Lord of the Rings","The Chronicles of Narnia","Moby-Dick","Jane Eyre","The Odyssey","Wuthering Heights","Harry Potter and the Philosopher's Stone","The Da Vinci Code","The Alchemist","The Kite Runner","The Little Prince","Gone with the Wind","One Hundred Years of Solitude","The Adventures of Tom Sawyer","The Grapes of Wrath","The Picture of Dorian Gray","A Tale of Two Cities","The Divine Comedy","The Color Purple","Les Misérables","The Hitchhiker's Guide to the Galaxy"],"Radhi Library")

choice = 'y'
while choice in ["y", "Y"]:
    print("\n********** Welcome to Radhi Library ***********\n")
    yourChoice = int(input("What would you like to do?\n\t1. Display Books\n\t2. Lend Books\n\t3. Add Books\n\t4. Return Book\n"))
    if yourChoice == 1:
        myLibrary.displayBooks()
    elif yourChoice == 2:
        myLibrary.lendBooks()
    elif yourChoice == 3:
        myLibrary.addBook()
    elif yourChoice == 4:
        myLibrary.returnBooks()
    else:
        print("Invalid Choice!, Please choose the right option.")

    choice = input("Type Y if you want to start continue... ")
