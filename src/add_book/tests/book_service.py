from book import Book


class BookService:
    def __init__(self, repository, validator):
        self.repository = repository
        self.validator = validator

    def addBook(self, title, author, isbn):
        # Xóa khoảng trắng thừa ở đầu và cuối
        title = title.strip()
        author = author.strip()
        isbn = isbn.strip()

        # Kiểm tra thông tin bị bỏ trống
        if not title or not author or not isbn:
            raise ValueError("Vui lòng nhập đầy đủ thông tin sách!")

        # Kiểm tra ISBN trùng
        if self.validator.is_duplicate(isbn):
            raise ValueError("ISBN đã tồn tại!")

        # Tạo sách mới
        book = Book(
            id=None,
            title=title,
            author=author,
            isbn=isbn
        )

        # Lưu sách và trả về kết quả
        return self.repository.save(book)