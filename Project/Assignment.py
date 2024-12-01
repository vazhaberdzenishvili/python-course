import datetime

class Book:
  def __init__(self, title, author, year ):
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    return f" '{self.title}' by {self.author}, published in {self.year}"
  
  
class BookManager: 
  def __init__(self, filename="Books.csv"):
    self.filename = filename
    self.books = [] 
    self.load_books()

  def add_book(self, title, author, year):
    while True:
      # Validate the year and ask for input again if invalid
      if not self.validate_year(year):
        year = input("\nPlease enter a valid year of publication: ")
      # Check if the book already exists in the collection
      else:
        if self.is_book_duplicate(title, author, year):
          print(f"\nBook '{title}' by {author} already exists \n")
          # Ask the user if they want to enter a different book
          user_input = input("Would you like to enter a different book? (y/n): ")
          if user_input.lower() != 'y':
            break
          title = input("Enter new book title: ")
          author = input("Enter new author name: ")
          year = input("Enter year of publication: ")
          
        else:
          # If it's not a duplicate, create a new book and save it
          new_book = Book(title, author, int(year))
          self.books.append(new_book)
          self.save_to_file()
          print(f"\nBook '{new_book.title}' added successfully")
          break

  def display_books(self):
    # Check if the books list is empty
    if not self.books:
      print("No books available")
    else:
      # Display all the books in the list
      for id, book in enumerate(self.books,1):
        print(f"{id}: {book}")
  
  def search_by_title(self, title):
    found = False
    for book in self.books:
      # If book title matches the search query, print it
      if title.lower() in book.title.lower():
        print(book)
        found = True
    if not found:
      print(f"Book with title '{title}' not found")

  def save_to_file(self):
    # Save the books list to the file
    with open(self.filename, 'w') as file:
      for book in self.books:
        file.write(f"{book.title},{book.author},{book.year}\n")

  def load_books(self):
    # Try to read the file and load books from it
    try:
      with open(self.filename, 'r') as file:
        for data in file:
          try:
            title, author, year = data.strip().split(',')
            year = int(year)
            self.books.append(Book(title.strip('"'), author.strip('"'), year))
          except ValueError:
            print(f"Invalid data")
    except FileNotFoundError:
      print("The Books file was not found")

  def is_book_duplicate(self, title, author, year):
    year = int(year)
    # Check if the book is already in the collection
    for book in self.books:
      if (book.title.lower() == title.lower() and
          book.author.lower() == author.lower() and
          book.year == year):
        return True
    return False
  
  def validate_year(self, year):
    # Check if the year is numeric and within the valid range
    if not year.isdigit() or year == '':
      print("Invalid input! Please enter a valid numeric year")
      return False
    
    year = int(year)
    current_year = datetime.datetime.now().year

    if 1800 <= year <= current_year:
      return True
    else:
      print(f"\nYear must be between 1800 and {current_year}. Please try again")
      return False
    
def main():
  manager = BookManager() # Initialize the book manager
  while True:
    # Display the options menu to the user
    print("\nChoose an option:")
    print("1) Add a new book")
    print("2) View all books")
    print("3) Search for a specific book")
    print("4) Exit the program")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      # Ask user for book details and add the book
      title = input("Enter book title: ")
      author = input("Enter author name: ")
      year = input("Enter year of publication: ")
      manager.add_book(title, author, year) 
    
    elif choice == '2':
      # Display all the books
      print()
      manager.display_books()
    
    elif choice == '3':
      # Search for a book by title
      title = input("Enter the title of the book to search: ")
      manager.search_by_title(title)
    
    elif choice == '4':
      print("Exit")
      break     

    else:
      print("Invalid choice! Please pick a number between 1 and 4")

if __name__ == "__main__":
  main()