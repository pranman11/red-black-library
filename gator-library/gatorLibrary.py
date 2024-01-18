import re
import sys
from library import GatorLibrary

def run_library():
    INSERT_BOOK = "InsertBook"
    PRINT_BOOK = "PrintBook"
    BORROW_BOOK = "BorrowBook"
    PRINT_BOOKS = "PrintBooks"
    RETURN_BOOK = "ReturnBook"
    FIND_CLOSEST_BOOK = "FindClosestBook"
    DELETE_BOOK = "DeleteBook"
    COLOR_FLIP_COUNT = "ColorFlipCount"
    QUIT = "Quit"

    fileName = sys.argv[1]
    input_file = open(fileName, 'r')
    try:
        gator_library = GatorLibrary()

        # For creating output file
        writer = create_file(fileName.split('.')[0])

        for new_line in input_file:
            command, arguements = extract_function_info(new_line)

            if command == INSERT_BOOK:
                gator_library.insert_book(
                    int(arguements[0]),
                    arguements[1][1:-1],
                    arguements[2][1:-1],
                    arguements[3][1:-1]
                )
            elif command == PRINT_BOOK:
                print_book_output = gator_library.print_book(int(arguements[0]))
                print(print_book_output)
                write_to_file(print_book_output, writer)
            elif command == BORROW_BOOK:
                patron_id = int(arguements[0])
                book_id = int(arguements[1])
                priority = int(arguements[2])
                borrow_book_output = gator_library.borrow_book(patron_id, book_id, priority)
                print(borrow_book_output)
                write_to_file(borrow_book_output, writer)
            elif command == PRINT_BOOKS:
                start_id = int(arguements[0])
                end_id = int(arguements[1])
                print_books_output = gator_library.print_books(start_id, end_id)
                print(print_books_output)
                write_to_file(print_books_output, writer)
            elif command == RETURN_BOOK:
                patron_id = int(arguements[0])
                book_id = int(arguements[1])
                return_book_output = gator_library.return_book(patron_id, book_id)
                print(return_book_output)
                write_to_file(return_book_output, writer)
            elif command == FIND_CLOSEST_BOOK:
                patron_id = int(arguements[0])
                closest_book_output = gator_library.find_closest_book(patron_id)
                print(closest_book_output)
                write_to_file(closest_book_output, writer)
            elif command == DELETE_BOOK:
                book_id = int(arguements[0])
                delete_book_output = gator_library.delete_book(book_id)
                print(delete_book_output)
                write_to_file(delete_book_output, writer)
            elif command == COLOR_FLIP_COUNT:
                color_flip_count_output = gator_library.color_flip_count()
                print(color_flip_count_output)
                write_to_file(color_flip_count_output, writer)
            elif command == QUIT:
                quit_output = "Program Terminated!!"
                print(quit_output)
                write_to_file(quit_output, writer)
                break

        writer.close()
    except Exception as e:
        print(e)
    finally:
        input_file.close()

def extract_function_info(code_string):
    # Define a regular expression pattern for matching function calls
    pattern = r'(\w+)\((.*)\)'
    
    # Use the findall method to extract all matches
    matches = re.findall(pattern, code_string)
    
    # Check if there are any matches
    if matches:
        # Each match is a tuple containing function name and parameters
        for match in matches:
            function_name, parameters = match
            # Split parameters into a list
            parameters_list = [param.strip() for param in parameters.split(',')]
            return function_name, parameters_list
    else:
        print("No function calls found in the given code string.")


def write_to_file(string, file):
    file.write(string + '\n')
    file.flush()


def create_file(input_file):
    file = open(input_file + "_output_file.txt", 'w')
    return file

def main():
    run_library()

if __name__ == "__main__":
    main()