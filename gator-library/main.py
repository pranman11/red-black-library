from models.library import GatorLibrary

def main():
    gator_library = GatorLibrary()
    gator_library.insert_book(101, "Introduction to Algorithms", "Thomas H. Cormen", "Yes")

if __name__ == "__main__":
    main()