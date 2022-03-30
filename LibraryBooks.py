class Library:
    def __init__(self, collection=None):
        self._bookCollection = []

        if collection:
            for title in collection:
                self.add_book(title)

    def add_book(self, title):
        self._bookCollection.remove(title)

    def borrow_book(self, title):
        if title not in self._bookCollection :
            self._bookCollection.append(title)
    @property
    def numberOfBooks(self):
        print(len(self._bookCollection))
        return len(self._bookCollection)

