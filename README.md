# Chức năng thêm sách mới – Nhóm 17

Đây là phần thực hiện User Story **Thêm sách mới** thuộc dự án **NHOM17-LIBRARY-MANAGEMENT-SYSTEM**.

## 1. User Story

> Là thủ thư, tôi muốn thêm sách mới vào hệ thống để quản lý tài sản thư viện.

Thông tin của một cuốn sách gồm:

| Thuộc tính | Ý nghĩa |
| --- | --- |
| `id` | Mã sách |
| `title` | Tên sách |
| `author` | Tác giả |
| `isbn` | Mã ISBN của sách |

## 2. Công nghệ sử dụng

- Python: xây dựng lớp dữ liệu và xử lý nghiệp vụ.
- Tkinter: thiết kế giao diện nhập sách.
- SQL: tạo bảng, thêm dữ liệu mẫu và truy vấn thông tin sách.

## 3. Cấu trúc thư mục

```text
src/add_book/
├── README.md
├── database/
│   └── book.sql
├── models/
│   └── book.py
├── repositories/
│   └── book_repository.py
├── validators/
│   └── isbn_validators.py
├── services/
│   └── book_service.py
└── ui/
    └── book_form.py
```

## 4. Các Technical Task

| Task | Nội dung | File thực hiện | Ước lượng |
| --- | --- | --- | --- |
| T1 | Thiết kế bảng Book và viết truy vấn SQL | `database/book.sql` | 1 giờ |
| T2 | Tạo lớp Book, hàm khởi tạo và getter/setter | `models/book.py` | 1 giờ |
| T3 | Lưu sách và tìm sách theo ISBN | `repositories/book_repository.py` | 1 giờ |
| T4 | Kiểm tra ISBN đã tồn tại | `validators/isbn_validators.py` | 1 giờ |
| T5 | Viết hàm thêm sách `addBook()` | `services/book_service.py` | 2 giờ |
| T6 | Thiết kế form nhập sách | `ui/book_form.py` | 4 giờ |
| T7 | Viết Unit Test cho chức năng thêm sách | Chưa có file kiểm thử | 2 giờ |

## 5. Nội dung từng phần

### T1 – Database

File `database/book.sql` gồm:

- Tạo bảng `Book` với bốn cột: `id`, `title`, `author`, `isbn`.
- Đặt `id` làm khóa chính.
- Đặt ràng buộc `UNIQUE` cho `isbn`.
- Thêm bốn cuốn sách mẫu.
- Xem toàn bộ sách.
- Tìm sách theo mã sách, ISBN, tên sách hoặc tác giả.
- Đếm tổng số sách.
- Sắp xếp sách theo tên.

Trong script hiện tại, `id` được nhập trực tiếp khi thêm dữ liệu.

### T2 – Lớp Book

File `models/book.py` định nghĩa lớp `Book`, gồm:

- Hàm khởi tạo nhận `id`, `title`, `author`, `isbn`.
- Getter để lấy thông tin.
- Setter để thay đổi thông tin.

### T3 – BookRepository

File `repositories/book_repository.py` cung cấp:

- `save(book)`: tự cấp mã và lưu sách.
- `find_by_isbn(isbn)`: tìm sách theo ISBN; trả về `None` nếu không tìm thấy.

Repository hiện lưu sách trong danh sách Python. Dữ liệu sẽ mất khi kết thúc chương trình.

### T4 – Kiểm tra ISBN trùng
