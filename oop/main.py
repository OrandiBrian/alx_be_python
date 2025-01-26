from book_class import Book

def main():
    # creating an instance of a book
    my_book = Book("1984", "George Orwell", 1949)

    # demonstrating the __str__ method
    print(my_book) # expected to use __str__

    # demonstrating the __repr__ method
    print(repr(my_book)) # expected to use __repr__

    # deleting a book instance to trigger __del__
    del my_book

if __name__ == '__main__':
    main()