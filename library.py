avlbooks = ["python", "java", "html", "c++"]


class library:

    def __init__(self, Avlbooks):
        self.books = Avlbooks

    def inputBooks(self, bookname):
        print(f"Thankyou for donating {bookname} book to MyLibrary")
        self.books.append(bookname)

    def availableBooks(self):
        print("Available books are: ")
        for books in self.books:
            print(f"* {books}")

    def issuebook(self, bookname):
        if bookname in self.books:
            print(
                f"{bookname} book has been issued. Please return it within 20 days.")
            self.books.remove(bookname)
        else:
            print(
                f"Sorry but {bookname} book is either issued to someone or it is not available. Please wait until it is available")

    def returnbook(self, bookname):
        print(f"{bookname} book has been returned.Thankyou for keeping it safe")
        self.books.append(bookname)


if __name__ == "__main__":
    user = library(avlbooks)

    while True:
        print("\n---Welcome to MyLibrary---")
        print("Please select options from below:\n1: Print available Books\n2: Add a book\n3: Issue a book\n4: Return a book\n5: Exit\n", end="")
        try:
            option = int(input("Enter your option here: "))
        except:
            print("Invalid option")

        if option == 1:
            user.availableBooks()

        elif option == 2:
            name = input("Enter the name of the book: ")
            name = name.lower()
            if name == "":
                print("Please Enter a valid name")
                False
            else:
                user.inputBooks(name)

        elif option == 3:
            user.issuebook(input("Enter the name of the book: "))
        elif option == 4:
            user.returnbook(input("Enter the name of the book: "))
        elif option == 5:
            print("Thankyou for using MyLibrary!!")
            exit()
        else:
            print("Please enter a valid option")
