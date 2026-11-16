import tkinter as tk
from tkinter import messagebox, ttk


class BookForm:
    def __init__(self, root, service):
        self.root = root
        self.service = service
        root.title("Thêm sách mới")
        root.resizable(False, False)

        frame = ttk.Frame(root, padding=24)
        frame.grid()
        ttk.Label(frame, text="THÊM SÁCH MỚI",
                  font=("Arial", 16, "bold")).grid(
                      row=0, column=0, columnspan=2, pady=(0, 18))

        self.title_var = tk.StringVar()
        self.author_var = tk.StringVar()
        self.isbn_var = tk.StringVar()
        fields = [("Tên sách:", self.title_var),
                  ("Tác giả:", self.author_var),
                  ("ISBN:", self.isbn_var)]

        for row, (label, variable) in enumerate(fields, start=1):
            ttk.Label(frame, text=label).grid(
                row=row, column=0, sticky="w", padx=(0, 12), pady=8)
            entry = ttk.Entry(frame, textvariable=variable, width=38)
            entry.grid(row=row, column=1, pady=8)
            if row == 1:
                self.title_entry = entry

        ttk.Button(frame, text="Thêm sách", command=self.add_book).grid(
            row=4, column=0, columnspan=2, pady=(18, 8))
        ttk.Label(frame, text="Dữ liệu chỉ được lưu trong lần chạy hiện tại.").grid(
            row=5, column=0, columnspan=2)
        root.bind("<Return>", lambda event: self.add_book())
        self.title_entry.focus_set()

    def add_book(self):
        try:
            book = self.service.addBook(
                self.title_var.get(),
                self.author_var.get(),
                self.isbn_var.get(),
            )
        except ValueError as error:
            messagebox.showerror("Không thể thêm sách", str(error), parent=self.root)
            return

        messagebox.showinfo(
            "Thành công",
            f"Đã thêm sách: {book.get_title()}\nMã sách: {book.get_id()}",
            parent=self.root,
        )
        self.title_var.set("")
        self.author_var.set("")
        self.isbn_var.set("")
        self.title_entry.focus_set()
