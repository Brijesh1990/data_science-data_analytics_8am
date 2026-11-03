
"""
=========================================================
             LIBRARY MANAGEMENT SYSTEM
                  Python + MySQL
=========================================================

Features:
1. Add Book
2. Display All Books
3. Search Book
4. Update Book
5. Delete Book
6. Manage Book Availability
7. Exit

Database : library_db
Table    : books

Author   : Python Student Project
=========================================================
"""

import mysql.connector
from mysql.connector import Error
# =========================================================
# DATABASE CONFIGURATION
# =========================================================

DB_HOST = "localhost"
PORT = 3306  # Default MySQL port
DB_USER = "root"
DB_PASSWORD = "admin"  # Change according to your MySQL password
DB_NAME = "library_db"


# =========================================================
# DATABASE CONNECTION
# =========================================================

def connect_database():

    try:
        # First connect to MySQL server without selecting a database
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )

        if connection.is_connected():

            cursor = connection.cursor()

            # Create database if it does not exist
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
            )

            cursor.close()
            connection.close()

            # Connect to the newly created database
            connection = mysql.connector.connect(
                host=DB_HOST,
                port=PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )

            print("\nDatabase connected successfully!")

            return connection

    except Error as e:
        print("\nDatabase Connection Error:", e)

        return None


# =========================================================
# CREATE TABLE
# =========================================================

def create_table():

    try:
        cursor = conn.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS books (
            book_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(150) NOT NULL,
            author VARCHAR(100) NOT NULL,
            category VARCHAR(100) NOT NULL,
            availability VARCHAR(20) DEFAULT 'Available'
        )
        """

        cursor.execute(query)

        conn.commit()

        cursor.close()

        print("Books table created successfully!")

    except Error as e:
        print("Table Creation Error:", e)


# =========================================================
# 1. ADD NEW BOOK (CREATE)
# =========================================================

def add_book():

    print("\n========== ADD NEW BOOK ==========")

    try:
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()
        category = input("Enter Book Category: ").strip()

        # Validate empty inputs
        if not title or not author or not category:
            print("\nAll fields are required!")
            return

        cursor = conn.cursor()

        query = """
        INSERT INTO books (title, author, category, availability)
        VALUES (%s, %s, %s, %s)
        """

        values = (title, author, category, "Available")

        cursor.execute(query, values)

        conn.commit()

        print("\nBook Added Successfully!")
        print("Generated Book ID:", cursor.lastrowid)

        cursor.close()

    except Error as e:
        print("Insert Error:", e)


# =========================================================
# 2. DISPLAY ALL BOOKS (READ)
# =========================================================

def display_books():

    print("\n================ ALL BOOK RECORDS ================")

    try:
        cursor = conn.cursor()

        query = "SELECT * FROM books ORDER BY book_id"

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            print("\nNo Book Records Found!")
            cursor.close()
            return

        # Display table headings
        print("-" * 105)

        print(
            f"{'ID':<8}"
            f"{'TITLE':<25}"
            f"{'AUTHOR':<22}"
            f"{'CATEGORY':<22}"
            f"{'STATUS':<15}"
        )

        print("-" * 105)

        # Display all book records
        for book in records:

            print(
                f"{book[0]:<8}"
                f"{book[1][:23]:<25}"
                f"{book[2][:20]:<22}"
                f"{book[3][:20]:<22}"
                f"{book[4]:<15}"
            )

        print("-" * 105)

        print("Total Books:", len(records))

        cursor.close()

    except Error as e:
        print("Display Error:", e)


# =========================================================
# 3. SEARCH BOOK BY ID (READ)
# =========================================================

def search_book():

    print("\n========== SEARCH BOOK ==========")

    try:
        book_id = int(input("Enter Book ID: "))

        cursor = conn.cursor()

        query = "SELECT * FROM books WHERE book_id = %s"

        cursor.execute(query, (book_id,))

        book = cursor.fetchone()

        if book:

            print("\nBook Found Successfully!")

            print("-" * 40)
            print("Book ID       :", book[0])
            print("Book Title    :", book[1])
            print("Author Name   :", book[2])
            print("Category      :", book[3])
            print("Availability  :", book[4])
            print("-" * 40)

        else:
            print("\nBook ID Not Found!")

        cursor.close()

    except ValueError:
        print("Please enter a valid numeric Book ID!")

    except Error as e:
        print("Search Error:", e)


# =========================================================
# 4. UPDATE BOOK DETAILS (UPDATE)
# =========================================================

def update_book():

    print("\n========== UPDATE BOOK DETAILS ==========")

    try:
        book_id = int(input("Enter Book ID to Update: "))

        cursor = conn.cursor()

        # Check whether the book exists
        cursor.execute(
            "SELECT * FROM books WHERE book_id = %s",
            (book_id,)
        )

        book = cursor.fetchone()

        if not book:
            print("\nBook ID Not Found!")
            cursor.close()
            return

        print("\nCurrent Book Details:")
        print("Title    :", book[1])
        print("Author   :", book[2])
        print("Category :", book[3])

        print("\nEnter New Details")
        print("(Press Enter to keep the existing value)")

        # Keep old values if the user enters nothing
        title = input("New Title: ").strip() or book[1]

        author = input("New Author: ").strip() or book[2]

        category = input("New Category: ").strip() or book[3]

        # Update book information
        query = """
        UPDATE books
        SET title = %s,
            author = %s,
            category = %s
        WHERE book_id = %s
        """

        values = (title, author, category, book_id)

        cursor.execute(query, values)

        conn.commit()

        print("\nBook Details Updated Successfully!")

        cursor.close()

    except ValueError:
        print("Please enter a valid numeric Book ID!")

    except Error as e:
        print("Update Error:", e)


# =========================================================
# 5. DELETE BOOK (DELETE)
# =========================================================

def delete_book():

    print("\n========== DELETE BOOK ==========")

    try:
        book_id = int(input("Enter Book ID to Delete: "))

        cursor = conn.cursor()

        # Check book before deleting
        cursor.execute(
            "SELECT title FROM books WHERE book_id = %s",
            (book_id,)
        )

        book = cursor.fetchone()

        if not book:

            print("\nBook ID Not Found!")

            cursor.close()
            return

        print("\nBook Title:", book[0])

        # Ask confirmation before deletion
        confirm = input(
            "Are you sure you want to delete this book? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            query = "DELETE FROM books WHERE book_id = %s"

            cursor.execute(query, (book_id,))

            conn.commit()

            print("\nBook Deleted Successfully!")

        else:

            print("\nDelete Operation Cancelled!")

        cursor.close()

    except ValueError:
        print("Please enter a valid numeric Book ID!")

    except Error as e:
        print("Delete Error:", e)


# =========================================================
# 6. UPDATE BOOK AVAILABILITY
# =========================================================

def update_availability():

    print("\n========== MANAGE BOOK AVAILABILITY ==========")

    try:
        book_id = int(input("Enter Book ID: "))

        cursor = conn.cursor()

        # Check whether book exists
        cursor.execute(
            "SELECT title, availability FROM books WHERE book_id = %s",
            (book_id,)
        )

        book = cursor.fetchone()

        if not book:

            print("\nBook ID Not Found!")

            cursor.close()
            return

        print("\nBook Title:", book[0])
        print("Current Status:", book[1])

        print("\n1. Available")
        print("2. Issued")

        choice = input("\nSelect New Availability: ").strip()

        if choice == "1":
            status = "Available"

        elif choice == "2":
            status = "Issued"

        else:
            print("\nInvalid Selection!")
            cursor.close()
            return

        # Update availability status
        query = """
        UPDATE books
        SET availability = %s
        WHERE book_id = %s
        """

        cursor.execute(query, (status, book_id))

        conn.commit()

        print("\nBook Availability Updated Successfully!")
        print("New Status:", status)

        cursor.close()

    except ValueError:
        print("Please enter a valid numeric Book ID!")

    except Error as e:
        print("Availability Error:", e)


# show availability pie chart
def show_availability_pie_chart():

    print("\n========== BOOK AVAILABILITY PIE CHART ==========")

    try:
        cursor = conn.cursor()

        # Count available and issued books
        cursor.execute(
            "SELECT availability, COUNT(*) FROM books GROUP BY availability"
        )

        records = cursor.fetchall()

        if not records:
            print("\nNo Book Records Found!")
            cursor.close()
            return

        # Prepare data for pie chart
        labels = []
        sizes = []

        for record in records:
            labels.append(record[0])
            sizes.append(record[1])

        # Plot pie chart
        import matplotlib.pyplot as plt

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Book Availability Distribution")
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

        cursor.close()

    except Error as e:
        print("Pie Chart Error:", e)

# =========================================================
# MAIN MENU
# =========================================================

def main_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("          LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Update Book Details")
        print("5. Delete Book")
        print("6. Manage Book Availability")
        print("7. Show Availability Pie Chart")
        print("8. Export All Books to Excel")
        print("9. Exit")

        print("=" * 50)

        choice = input("Enter Your Choice (1-9): ").strip()

        if choice == "1":

            add_book()

        elif choice == "2":

            display_books()

        elif choice == "3":

            search_book()

        elif choice == "4":

            update_book()

        elif choice == "5":

            delete_book()

        elif choice == "6":

            update_availability()

        elif choice == "7":

            show_availability_pie_chart()

        elif choice == "8":

            export_to_excel()

        elif choice == "9":

            print("\nThank You for Using Library Management System!")

            break

        else:

            print("\nInvalid Choice! Please Select Between 1-9.")


# generate excel file with all books
def export_to_excel():
    
    print("\n========== EXPORT ALL BOOKS TO EXCEL ==========")

    try:
        cursor = conn.cursor()

        query = "SELECT * FROM books ORDER BY book_id"

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            print("\nNo Book Records Found!")
            cursor.close()
            return

        # Create a DataFrame using pandas
        import pandas as pd

        df = pd.DataFrame(records, columns=["Book ID", "Title", "Author", "Category", "Availability"])

        # Export to Excel
        excel_file = "library_books.xlsx"
        df.to_excel(excel_file, index=False)

        print(f"\nAll Book Records Exported Successfully to '{excel_file}'!")

        cursor.close()

    except Error as e:
        print("Export Error:", e)

# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

if __name__ == "__main__":

    # Establish database connection
    conn = connect_database()

    # Start application only if connection is successful
    if conn is not None:

        try:
            # Create books table
            create_table()

            # Run the main menu
            main_menu()

        except KeyboardInterrupt:
            print("\n\nApplication Interrupted!")

        finally:
            # Close database connection safely
            if conn.is_connected():
                conn.close()

                print("\nMySQL Connection Closed.")

    else:

        print("\nUnable to Start Application.")
        print("Please Check Your MySQL Server and Credentials.")
