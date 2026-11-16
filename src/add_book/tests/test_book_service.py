import unittest

from book_repository import BookRepository
from isbn_validator import ISBNValidator
from book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self):
        # Tạo kho sách mới cho mỗi lần kiểm thử
        self.repository = BookRepository()
        self.validator = ISBNValidator(self.repository)

        self.service = BookService(
            self.repository,
            self.validator
        )

    def test_them_sach_thanh_cong(self):
        book = self.service.addBook(
            "Lập trình Python",
            "Nguyễn Văn A",
            "9786040000001"
        )

        self.assertEqual(book.get_id(), 1)
        self.assertEqual(book.get_title(), "Lập trình Python")
        self.assertEqual(book.get_author(), "Nguyễn Văn A")
        self.assertEqual(book.get_isbn(), "9786040000001")

        saved_book = self.repository.find_by_isbn(
            "9786040000001"
        )

        self.assertIs(saved_book, book)

    def test_tu_choi_isbn_trung(self):
        original = self.service.addBook(
            "Lập trình Python",
            "Nguyễn Văn A",
            "9786040000001"
        )

        with self.assertRaisesRegex(ValueError, "ISBN đã tồn tại"):
            self.service.addBook(
                "Lập trình Java",
                "Trần Văn B",
                "9786040000001"
            )

        # Lần thêm bị từ chối không làm tăng số lượng sách
        self.assertEqual(len(self.repository.books), 1)

        saved_book = self.repository.find_by_isbn(
            "9786040000001"
        )

        self.assertIs(saved_book, original)


if __name__ == "__main__":
    unittest.main()