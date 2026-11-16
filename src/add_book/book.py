class Book:
    # Hàm khởi tạo thông tin sách
    def __init__(self, id, title, author, isbn):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn

    # Các hàm lấy thông tin (getter)
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    # Các hàm cập nhật thông tin (setter)
    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_isbn(self, isbn):
        self.isbn = isbn


# Chạy thử khi mở trực tiếp file book.py
if __name__ == "__main__":
    book = Book(
        1,
        "Lập trình Python",
        "Nguyễn Văn An",
        "9786040000001"
    )

    print("Mã sách:", book.get_id())
    print("Tên sách:", book.get_title())
    print("Tác giả:", book.get_author())
    print("ISBN:", book.get_isbn())

    book.set_title("Lập trình Python cơ bản")
    print("Tên sách sau khi sửa:", book.get_title())