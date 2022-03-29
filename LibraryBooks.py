class Library:
    number_of_books = 0
    bookList = []

    def __init__(self, title):
        self.title = title
        Library.bookList.append(title)
        Library.number_of_books += 1

    @property
    def book(self, title):
        for b in Library.bookList:
            if b != title:
                Library.bookList.pop(title)

    @book.setter
    def book(self, title):
        if title == self.title:
            #raise ValueError("Ta książka jest już w bazie")
            print("Ta książka już jest")


    def show_books(self):
        print(Library.bookList)


book1 = Library("Bolek i Lolek")
book2 = Library("Python")
book3 = Library("Python")
print (Library.bookList)