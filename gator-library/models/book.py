from utilities.min_heap import MinBinaryHeap

class Book:
    #tested            
    def __init__(self, book_id, book_name="", author_name="", availability_status=True, borrowed_by=None):
        self.book_id = book_id
        self.book_name = book_name if book_name else str(book_id)
        self.author_name = author_name
        self.availability_status = availability_status
        self.borrowed_by = borrowed_by    # patron ID of the patron in possession of the book
        self.reservation_heap = MinBinaryHeap()

    def borrow_book(self, patron_id, patronPriority) -> str:
        if self.availability_status:
            self.borrowed_by = patron_id
            return f"Book {self.book_id} Borrowed by Patron {patron_id}"

        self.reservation_heap.add(patron_id, patronPriority)
        return f"Book {self.book_id} Reserved by Patron {patron_id}"

    def return_book(self, patron_id):            
        if self.reservation_heap.get_root() == None:
            self.borrowed_by = None
            return f"Book {self.book_id} Returned by Patron {patron_id}"
        next_patron_node = self.reservation_heap.remove_min()
        self.borrowed_by = next_patron_node.data
        return f"\nBook {self.book_id} Allotted to Patron {self.borrowed_by}"