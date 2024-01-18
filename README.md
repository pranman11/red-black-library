# red-black-library

Red-Black-Library is an efficient library management system that manages its books and patrons. It 
allows patrons to borrow or reserve books based on priority and then return them. Moreover,
you can add new books, delete old books and efficiently search book data based on book ID.
The efficiency of the system is due to the use of a Red-Black tree data structure to ensure
storage and management of the books.

A priority-queue mechanism using Binary Min-heaps is implemented as well – a data structure
for managing book reservations in case a book is not currently available to be borrowed. Each
book will have its own min-heap to keep track of book reservations made by the patrons.

The software system is implemented in Python using object-oriented design. There are 2 main classes 
that represent the Library (GatorLibrary) and Books (Book), and the other classes represent
implementation of internal data structures - RedBlackTree and MinBinaryHeap. Apart from 
supporting all basic operations - search, searching books closest to a book ID, searching within a 
range of IDs, insert, and delete, the Red Black Tree also counts and displays the number of 
color flips occuring while balancing after insertion or deletion.

To test this program you have to create a test file with the commands and pass the filename
while running the program. You can find sample test and output files in the repository as well.

- The code can be run with the command "python gatorLibrary.py <file_name>"
- The output will be generated in the file <filename>_output_file.txt
