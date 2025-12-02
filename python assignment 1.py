# Name: Kamal Prajapati
# Roll No: 2501660048
# Course: BCA Cybersecurity
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-2 Mini Project
# Title: Library Book Manager
# Date: 2024-12-19

# Initialize data structures
books = {
    "B101": {"title": "Python Programming", "author": "Guido Van Rossum", "copies": 5},
    "B102": {"title": "Data Structures", "author": "Cormen", "copies": 3},
    "B103": {"title": "Cyber Security", "author": "William Stallings", "copies": 4},
    "B104": {"title": "Web Development", "author": "Jon Duckett", "copies": 2},
    "B105": {"title": "Database Systems", "author": "Ramez Elmasri", "copies": 6}
}

borrowed_books = {}

# Functions for different operations
def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("              MAIN MENU")
    print("=" * 50)
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Borrowed Books")
    print("7. Exit")
    print("=" * 50)

def add_book():
    """Add new book to library"""
    print("\n--- ADD NEW BOOK ---")
    
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Error: Book ID already exists!")
        return
    
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    try:
        copies = int(input("Enter Number of Copies: "))
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    
    books[book_id] = {"title": title, "author": author, "copies": copies}
    print(f"Book '{title}' added successfully!")

def view_books():
    """Display all books in tabular format"""
    print("\n--- ALL BOOKS IN LIBRARY ---")
    print("-" * 80)
    print(f"{'Book ID':<10} {'Title':<25} {'Author':<20} {'Copies':<10}")
    print("-" * 80)
    
    for book_id, details in books.items():
        print(f"{book_id:<10} {details['title']:<25} {details['author']:<20} {details['copies']:<10}")
    print("-" * 80)

def search_book():
    """Search books by ID or Title"""
    print("\n--- SEARCH BOOK ---")
    print("1. Search by Book ID")
    print("2. Search by Title")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        book_id = input("Enter Book ID: ")
        if book_id in books:
            print("Book Found!")
            print(f"Book ID: {book_id}")
            print(f"Title: {books[book_id]['title']}")
            print(f"Author: {books[book_id]['author']}")
            print(f"Available Copies: {books[book_id]['copies']}")
        else:
            print("Book Not Found!")
    
    elif choice == "2":
        title_search = input("Enter book title to search: ").lower()
        found_books = []
        
        for book_id, details in books.items():
            if title_search in details['title'].lower():
                found_books.append((book_id, details))
        
        if found_books:
            print(f"Found {len(found_books)} book(s):")
            for book_id, details in found_books:
                print(f"ID: {book_id} | Title: {details['title']} | Author: {details['author']} | Copies: {details['copies']}")
        else:
            print("No books found with that title!")
    
    else:
        print("Invalid choice!")

def borrow_book():
    """Borrow book system"""
    print("\n--- BORROW BOOK ---")
    
    student_name = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")
    
    if book_id not in books:
        print("Error: Book ID not found!")
        return
    
    if books[book_id]['copies'] <= 0:
        print("Error: No copies available!")
        return
    
    if student_name in borrowed_books:
        print("Error: Student already has a borrowed book!")
        return
    
    books[book_id]['copies'] -= 1
    borrowed_books[student_name] = book_id
    
    print(f"Success! {student_name} borrowed '{books[book_id]['title']}'")
    print(f"Remaining copies: {books[book_id]['copies']}")

def return_book():
    """Return book system"""
    print("\n--- RETURN BOOK ---")
    
    student_name = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")
    
    if student_name not in borrowed_books:
        print("Error: No record found for this student!")
        return
    
    if borrowed_books[student_name] != book_id:
        print("Error: This student didn't borrow the specified book!")
        return
    
    books[book_id]['copies'] += 1
    del borrowed_books[student_name]
    
    print(f"Success! {student_name} returned '{books[book_id]['title']}'")
    print(f"Available copies now: {books[book_id]['copies']}")

def view_borrowed_books():
    """Display borrowed books using list comprehension"""
    print("\n--- CURRENTLY BORROWED BOOKS ---")
    
    if not borrowed_books:
        print("No books are currently borrowed!")
        return
    
    borrowed_list = [f"{student} -> {books[book_id]['title']} (ID: {book_id})" 
                    for student, book_id in borrowed_books.items()]
    
    print("\n".join(borrowed_list))

def save_to_file():
    """Save library data to file"""
    try:
        with open("library_data.txt", "w") as file:
            file.write("LIBRARY BOOKS DATA\n")
            file.write("=" * 50 + "\n")
            for book_id, details in books.items():
                file.write(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}\n")
            
            file.write("\nBORROWED BOOKS\n")
            file.write("=" * 50 + "\n")
            for student, book_id in borrowed_books.items():
                file.write(f"Student: {student}, Book ID: {book_id}\n")
        
        print("Data saved to 'library_data.txt'")
    except Exception as e:
        print(f"Error saving file: {e}")

# Main program loop
def main():
    print("=" * 60)
    print("           LIBRARY BOOK MANAGEMENT SYSTEM")
    print("=" * 60)
    print("Welcome to KRMU Library Management System")
    print()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            view_borrowed_books()
        elif choice == "7":
            save_to_file()
            print("\nThank you for using Library Management System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-7")
        
        input("\nPress Enter to continue...")

# Run the program
if _name_ == "_main_":
    main()
