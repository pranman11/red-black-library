from min_heap import MinBinaryHeap

class Book:
    def __init__(self, book_id, book_name="", author_name="", availability_status="Yes", borrowed_by=None):
        self.book_id = book_id
        self.book_name = book_name if book_name else str(book_id)
        self.author_name = author_name
        self.availability_status = availability_status
        self.borrowed_by = borrowed_by    # patron ID of the patron in possession of the book
        self.reservation_heap = MinBinaryHeap()

    def borrow_book(self, patron_id, patron_priority) -> str:
        if self.availability_status == "Yes":
            self.borrowed_by = patron_id
            self.availability_status = "No"
            return f"Book {self.book_id} Borrowed by Patron {patron_id}\n"

        self.reservation_heap.add(patron_id, patron_priority)
        return f"Book {self.book_id} Reserved by Patron {patron_id}\n"

    def return_book(self, patron_id):            
        if self.reservation_heap.get_root() == None:
            self.borrowed_by = None
            self.availability_status = "Yes"
        output = f"Book {self.book_id} Returned by Patron {patron_id}\n"
        next_patron_node = self.reservation_heap.remove_min()
        if next_patron_node:
            self.borrowed_by = next_patron_node.data
            output += f"\nBook {self.book_id} Allotted to Patron {self.borrowed_by}\n"
        return output