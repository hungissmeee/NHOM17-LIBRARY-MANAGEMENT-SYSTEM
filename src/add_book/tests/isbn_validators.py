class ISBNValidator:
    def __init__(self, repository):
        self.repository = repository

    def is_duplicate(self, isbn):
        isbn = isbn.strip()

        book = self.repository.find_by_isbn(isbn)

        # Tìm thấy sách thì ISBN đã tồn tại
        return book is not None