# DISCLAIMER to dear users and dear Global AI Mentors
# Do not use any special characters while adding or removing a book
# Try to type English, not any other languages

# Note: I have not used any translated text or AI generated code on this worksheet
# GitHub: github.com/korayalkan
# LinkedIn: linkedin.com/in/korayalkankarakoc/

# Importing the required libraries / modules
from time import sleep

# Creating the Library Class
class Library:

    def __init__(self):

        # To list all the books, we will use this dict (updated version of 'books.txt')
        self.books = {
            'Book Name': [],
            'Author': [],
            'Release Year': [],
            'Page Number': []
        }
        self.createTextFile()   # Defining function to create a text file



    # Create a text file when program starts
    def createTextFile(self):

        # Importing the libraries to use only in this function
        # Doing this will help us in bigger projects
        # We don't want to import hundreds of heavy libraries on top, just to use in 1 function
        import os

        # Defining our file  name here
        fileName = 'books.txt'

        # If file does not exist
        if not os.path.exists(fileName):
            print(f'Checking the "{fileName}"...')

            # Creating the text file
            with open(fileName, 'a+'):
                sleep(1.5)  # Adding sleep funcs here just for better visuals on console
                print(f'Could not find and created "{fileName}" !\n')
                sleep(1.5)
                print(f'Redirecting to main menu...\n')
                sleep(2)

        # If file already exists
        else:
            print(f'Redirecting to main menu...\n')
            sleep(2)

        # Opening and reading the text file to list
        with open('books.txt', 'r') as textFile:
            read = textFile.readlines()

            # Delete new line "\n" characters
            for data in read:
                a, b, c, d = data.split(',')
                d = d.strip('\n')

                # Add author, book names, release year and page numbers to the book list
                self.books['Book Name'].append(a)
                self.books['Author'].append(b)
                self.books['Release Year'].append(c)
                self.books['Page Number'].append(d)



    # List all the authors and book names in Library
    def listBooks(self):

        # If library is empty
        if int(len(self.books['Author'])) < 1:
            sleep(1.5)
            print('\nThe library is empty!\n')
            sleep(1)
            print('Please add a new book!\n')
            sleep(2)
            return main()  # Return to beginning

        # List, print the books
        print('\tAuthor \t\t|\t Book Name')
        print('-'*35)

        i = 0   # i = 0 for list indexing
        for author in self.books['Author']:
            print(author, '\t\t', self.books['Book Name'][i])
            i += 1

        # Add a newline
        # Lastly, a little sleep function for 'Redirecting to main menu' message
        print('\n')
        sleep(1.5)



    # Add a new book to the Library
    def addNewBook(self):

        # Global statements
        global bookNames, authors, releaseYears, pageNumbers

        # Here, getting inputs from user
        try:
            # Using "title()" to capitalize first letter of every word of author's name
            authors = input('Enter the author: ').title()
            # If author is empty
            if not authors:
                print('Author cannot be empty!\n')
                return self.addNewBook()    # Return to beginning

            # Using "title()" to capitalize first letter of each word
            # Because I don't want user to add an existing book
            bookNames = input('Enter the book name: ').title()
            # If book name is empty
            if not bookNames:
                print('Book name cannot be empty!\n')
                return self.addNewBook()    # Return to beginning

            # Checking if book exists in 'books.txt'
            elif bookNames in self.books['Book Name']:
                print('Book already exists!\n')
                return self.addNewBook()    # Return to beginning

            releaseYears = int(input("Enter the release year: "))
            # If release year is not integer or less than 0
            if not isinstance(releaseYears, int) or releaseYears < 0:
                print("Release year must be a positive integer!\n")
                return self.addNewBook()    # Return to beginning

            pageNumbers = int(input("Enter the number of pages: "))
            # If page number is not integer or less than 0
            if not isinstance(pageNumbers, int) or pageNumbers < 1:
                print("Page numbers must be a positive integer!\n")
                return self.addNewBook()    # Return to beginning

        # Handling the ValueError exception
        except ValueError as ve:
            print(f'Error: {ve} \n')
            return self.addNewBook()    # Return to beginning

        # If everything is correct, add the new book to the 'books.txt'
        finally:
            # Open the 'books.txt' and append new book's content
            with open('books.txt', 'a+') as textFile:
                textFile.writelines(bookNames)
                textFile.writelines(', ')
                textFile.writelines(authors)
                textFile.writelines(', ')
                textFile.writelines(str(releaseYears))
                textFile.writelines(', ')
                textFile.writelines(str(pageNumbers))
                textFile.writelines('\n')

            # Give user a message if adding is successful
            print(f'\nYour book "{bookNames}" has successfully added to the library!\n')
            sleep(1.5)



    # Remove book from the library
    def removeBook(self):

        # Global statements
        global userInput

        # If library is empty
        if int(len(self.books['Author'])) < 1:
            sleep(1.5)
            print('\nThe library is empty!\n')
            sleep(2)
            return main()   # Return to beginning

        try:
            # Getting user input with "title()" function because
            # We stored book names with "title()" function in "self.addNewBook()" function
            userInput = input('Enter a book name to delete: ').title()

            # If userInput (Book Name) is empty
            if not userInput:
                print('Book name cannot be empty!\n')
                return self.removeBook()    # Return to beginning

            # If book does not exist in library
            elif userInput not in self.books['Book Name']:
                print(f'Book "{userInput}" does not exist in library!\n')
                return self.removeBook()    # Return to beginning

            # If book exists, remove it in here
            elif userInput in self.books['Book Name']:
                sleep(1.5)
                print(f'\nBook "{userInput}" exists in library!\n')
                sleep(1.5)
                print(f'Removing the book "{userInput}" from the Library...')
                sleep(2.50)
                print('Done!\n')
                sleep(2)

        # Handling the ValueError exception
        except ValueError as ve:
            print(f'Error: {ve} \n')
            return self.removeBook()    # Return to beginning

        finally:
            # Finding the index of the book name in self.books to remove it's content
            indexToRemove = self.books['Book Name'].index(userInput)

            # Remove the contents of book from self.books
            del self.books['Book Name'][indexToRemove]
            del self.books['Author'][indexToRemove]
            del self.books['Release Year'][indexToRemove]
            del self.books['Page Number'][indexToRemove]

            # For only 1 time, let's clear the 'books.txt' file to rewrite it
            with open('books.txt', 'w') as textFile:
                textFile.truncate(0)

            i = 0   # i = 0 for list indexing
            # Rewrite the 'books.txt' to update the file
            for author in self.books['Author']:

                # If there is nothing to rewrite in books as content
                # Just add a newline to the 'books.txt'
                if int(len(self.books['Author'])) == 0:
                    with open('books.txt', 'a+') as textFile:
                        textFile.writelines('\n')
                        return main()   # Return to beginning

                # j for writing the newline '\n' characters at the end of the line
                # If I add '\n' everytime, reading the file and appending might be a problem in the future
                # j = len(self.books['Author'])

                # If the list is not empty, rewrite it
                elif int(len(self.books['Author'])):
                    # Open the 'books.txt' and rewrite everything left in self.books
                    with open('books.txt', 'a+') as textFile:
                        textFile.writelines(self.books['Book Name'][i])
                        textFile.writelines(', ')
                        textFile.writelines(self.books['Author'][i])
                        textFile.writelines(', ')
                        textFile.writelines(self.books['Release Year'][i])
                        textFile.writelines(', ')
                        textFile.writelines(self.books['Page Number'][i])
                        textFile.writelines('\n')

                        i += 1  # Add 1 to i on every step of loop

                    # This is for newline characters, add it until the last step
                    # It shouldn't add '\n' on the last step because, while adding a new book, we also start with '\n'
                    # This might cause reading and writing problems for our text file
                    # while j - i != 0:
                    #     textFile.writelines('\n')
                    #     break   # Stop the while loop



# Main function here
def main():

    # Our object
    lib = Library()

    try:

        # Global statements
        global userData

        # Let's get the user data here and create a menu
        userData = int(input('=-=-= MENU =-=-=\n'
                        '1) List Books\n'
                        '2) Add Book\n'
                        '3) Remove Book\n'
                        '4) Save & Exit'
                        ': '))

        # If userData is empty
        if not userData:
            print(f'Invalid input!\n')
            return main()   # Return to beginning

        # If userData is not integer and not between 1-4
        elif int(userData) > 4 or int(userData) < 1:
            print(f'Try to enter an integer between 1-4!\n')
            return main()   # Return to beginning

    # Handling the ValueError exception
    except ValueError as ve:
        print(f'Error: {ve} \n')
        return main()   # Return to beginning

    finally:
        # If user wants to list books
        if userData == 1:
            lib.listBooks()     # Call object and run the listBooks function
            return main()   # Return to beginning

        # If user wants to add book
        elif userData == 2:
            lib.addNewBook()    # Call object and run the addNewBook function
            return main()   # Return to beginning

        # If user wants to remove a book
        elif userData == 3:
            lib.removeBook()    # Call object and run the removeBook function
            return main()   # Return to beginning

        # If user wants to quit and save the changes
        elif userData == 4:
            print('\nSaving changes..')
            sleep(1.5)
            print('Exiting...')
            sleep(1.5)
            exit()  # Exit the program




# Run the main function / program
main()
