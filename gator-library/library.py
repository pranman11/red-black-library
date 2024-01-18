from red_black_tree import RedBlackTree
from book import Book

class GatorLibrary:
    def __init__(self):
        self.library_tree = RedBlackTree()

    def print_book(self, book):
        if isinstance(book, int):
            book_node = self.library_tree.search(book)
            if book_node:
                book = book_node.data
            else:
                return f"Book {book} not found in the library\n"
        return f"BookId = {book.book_id}\nTitle = {book.book_name}\nAuthor = {book.author_name}\nAvailability = {book.availability_status}\nBorrowedBy = {book.borrowed_by}\nReservations = {book.reservation_heap.get_heap_data()}\n"

    def print_books(self, book_id1, book_id2):
        books = self.library_tree.search_between(book_id1, book_id2)
        if len(books) == 0:
            return "No Books in the specified range.\n"
        book_list = ""
        for book in books:
            book_list += self.print_book(book) + "\n"
        return book_list

    def insert_book(self, book_id, book_name, author_name, availability_status, borrowed_by = 0):
        book = Book(book_id, book_name, author_name, availability_status, borrowed_by)
        self.library_tree.insert(book)
        return ""

    def borrow_book(self, patron_id, book_id, patron_priority):
        book_node = self.library_tree.search(book_id)
        return book_node.data.borrow_book(patron_id, patron_priority) if book_node else ""

    def return_book(self, patron_id, book_id):
        book_node = self.library_tree.search(book_id)
        return book_node.data.return_book(patron_id) if book_node else ""

    def delete_book(self, book_id):
        deleted_book = self.library_tree.delete(book_id)
        output = f"Book {book_id} is no longer available."
        reserved_patrons = []
        while deleted_book.reservation_heap.get_root() != None:
            reserved_patrons.append(deleted_book.reservation_heap.remove_min().data)
        if reserved_patrons:
            if len(reserved_patrons) == 1:
                output += f" Reservation made by patron {reserved_patrons[0]} has been cancelled!"
                return output
            
            output += f" Reservations made by patrons "
            output += ", ".join([str(rp) for rp in reserved_patrons])
            output += " have been cancelled!"
        return output + "\n"

    def find_closest_book(self, book_id):
        closest_match_books = self.library_tree.search_closest(book_id)
        book_list = ""
        for book in closest_match_books:
            book_list += self.print_book(book) + "\n"
        return book_list

    def color_flip_count(self):
        return f"Color Flip Count: {self.library_tree.color_flip_count}\n"
    
    