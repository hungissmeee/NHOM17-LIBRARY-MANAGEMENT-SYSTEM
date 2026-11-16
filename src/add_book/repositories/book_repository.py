class BookRepository:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def save(self, book):
        # Tự động cấp mã cho sách mới
        book.set_id(self.next_id)
        self.next_id += 1

        self.books.append(book)
        return book

    def find_by_isbn(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                return book

        return None