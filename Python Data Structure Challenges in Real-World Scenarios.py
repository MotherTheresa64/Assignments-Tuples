# Task 1: Library System Enhancement

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_books(library, new_books):
    # Convert the library list to a set
    library_set = set(library)
    # Add new books to the set (duplicates will be ignored)
    library_set.update(new_books)
    # Convert the set back to a list
    updated_library = list(library_set)
    return updated_library
# New books to add
new_books = [("Brave New World", "Aldous Huxley"), ("The Great Gatsby", "F. Scott Fitzgerald")]
# Update the library
library = add_books(library, new_books)
print(library)