# Library Management System

This project implements a Library Management System using object-oriented programming techniques in Python. The program utilizes a database stored in the "books.txt" file, where each line represents a single book, including information such as book name, author, release date, and number of pages.

## Features:

### Library Class:

- Constructor method opens the "books.txt" file, and destructor method closes the file.
- If "books.txt" is not created previously, the constructor with "a+" mode will create the file.

### Library Methods:

- **List Books:**
  - Reads the contents of the file and prints book names and authors.
  - If file is empty, warns the user to add a new book.
- **Add Book:**
  - Adds a new book to the "books.txt" file based on user input.
  - You can not add the same book twice.
- **Remove Book:**
  - Deletes a book with the given title from the "books.txt" file.
  - If the file is empty, informs the user as 'Library is empty!'.
  - You can not delete a non-existing book.

### Usage:

- Create a "Library" object named "lib."
- Interact with the "lib" object through a menu-driven interface.

### Menu Options:

1. **List Books:**
   - Display a list of all books in the database.
2. **Add Book:**
   - Add a new book to the database.
3. **Remove Book:**
   - Remove a book from the database.
4. **Exit:**
   - Exit the program.

## Instructions:

1. Clone the repository.
2. Run the program and interact with the Library Management System through the menu.
3. Explore and modify the code as needed.
4. Feel free to contribute and enhance the functionality of this Library Management System!
