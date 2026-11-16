class Book:
    def __init__(self, id, title, author, isbn):
        self._id = id
        self._title = title
        self._author = author
        self._isbn = isbn

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn
