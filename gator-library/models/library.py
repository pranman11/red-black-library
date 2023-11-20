from utilities.red_black_tree import RedBlackTree
from .book import Book

class GatorLibrary:
    def __init__(self):
        self.library_tree = RedBlackTree()

    def print_book(self, book):
        if isinstance(book, int):
            book_node = self.library_tree.search_tree(book)
            book = book_node.data
        return f"BookId = {book.book_id} Title = {book.book_name} Author = {book.author_name} Availability = {book.availability_status} BorrowedBy = {book.borrowed_by} Reservations = {book.reservation_heap.get_heap_data()}"

    def print_books(self, book_id1, book_id2):
        books = self.library_tree.search_tree(book_id1, book_id2)
        if len(books) == 0:
            return "No Books in the specified range."
        book_list = ""
        for book in books:
            book_list += self.print_book(book)
        return book_list

    #tested
    def insert_book(self, book_id, book_name, author_name, availability_status, borrowed_by = 0):
        book = Book(book_id, book_name, author_name, availability_status, borrowed_by)
        self.library_tree.insert(book)
        print(self.print_book(book))

    def borrow_book(self, patron_id, book_id, patron_priority):
        book_node = self.library_tree.search_tree(book_id)
        return book_node.data.borrow_book(patron_id, patron_priority)

    def return_book(self, patron_id, book_id):
        book_node = self.library_tree.search_tree(book_id)
        return book_node.data.return_book(patron_id)

    def delete_book(self, book_id):
        deleted_book = self.library_tree.delete(book_id)
        output = f"Book {book_id} is no longer available."
        reserved_patrons = []
        while deleted_book.reservation_heap.get_root() != None:
            reserved_patrons.add(deleted_book.reservation_heap.remove_min().data)
            if len(reserved_patrons) == 1:
                # null check??
                output += f"Reservation made by patron {reserved_patrons[0]} has been cancelled!"
            output += f" Reservations made by patrons "
            output += ", ".join(reserved_patrons)
            output += " have been cancelled!"
        return output

    def find_closest_book(self, book_id):
        closest_match_books = self.library_tree.search_closest(book_id)
        book_list = " "
        for book in closest_match_books:
            book_list += self.print_book(book)
        return book_list

    def color_flip_count(self):
        return f"Color Flip Count: {self.library_tree.color_flip_count}"