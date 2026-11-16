-- T1: TAO BANG BOOK, THEM DU LIEU VA TRUY VAN

-- 1. Tao bang Book
-- id duoc nhap truc tiep khi them sach.
CREATE TABLE Book (
    id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(13) NOT NULL,

    CONSTRAINT PK_Book PRIMARY KEY (id),
    CONSTRAINT UQ_Book_ISBN UNIQUE (isbn)
);

-- 2. Them du lieu mau
INSERT INTO Book (id, title, author, isbn)
VALUES
    (1, 'Lap trinh Python', 'Nguyen Van An', '9786040000001'),
    (2, 'Co so du lieu', 'Tran Van Binh', '9786040000002'),
    (3, 'Cong nghe phan mem', 'Le Thi Hoa', '9786040000003'),
    (4, 'Python co ban', 'Nguyen Van An', '9786040000004');

-- 3. Xem tat ca sach
SELECT id, title, author, isbn
FROM Book;

-- 4. Tim sach theo id
SELECT id, title, author, isbn
FROM Book
WHERE id = 1;

-- 5. Tim sach theo ISBN
SELECT id, title, author, isbn
FROM Book
WHERE isbn = '9786040000001';

-- 6. Tim sach theo tu khoa trong ten
SELECT id, title, author, isbn
FROM Book
WHERE title LIKE '%Python%';

-- 7. Tim sach theo tac gia
SELECT id, title, author, isbn
FROM Book
WHERE author = 'Nguyen Van An';

-- 8. Dem tong so sach
SELECT COUNT(*) AS tong_so_sach
FROM Book;

-- 9. Sap xep danh sach theo ten sach
SELECT id, title, author, isbn
FROM Book
ORDER BY title ASC;