class Book:

    id = 1 # Class property
    book_list = []

    # every book should have a title, author and id
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.id = Book.id
        Book.book_list.append(self)
        # increment the id
        Book.id += 1

    @classmethod
    def find(cls,id):
        return [book for book in cls.book_list if book.id == id][0]