
import sqlite3
from database import get_connection
# CREATE: Add a new student
def add_student(name, email, phone, course, city):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (name, email, phone, course, city)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, course, city))

        conn.commit()

        print("\nStudent added successfully!")
        print("Student ID:", cursor.lastrowid)

    except sqlite3.IntegrityError:
        print("\nError: Email already exists!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()


# READ: Display all students
def display_students():

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("\nNo student records found!")
            return

        print("\n" + "=" * 95)
        print("                  STUDENT RECORDS")
        print("=" * 95)

        # Display table headings
        print(
            f"{'ID':<5}"
            f"{'Name':<20}"
            f"{'Email':<25}"
            f"{'Phone':<15}"
            f"{'Course':<15}"
            f"{'City':<15}"
        )

        print("-" * 95)

        # Display student records
        for student in students:

            print(
                f"{student['id']:<5}"
                f"{student['name']:<20}"
                f"{student['email']:<25}"
                f"{student['phone']:<15}"
                f"{student['course']:<15}"
                f"{student['city']:<15}"
            )

        print("=" * 95)

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()




# UPDATE: Modify existing student information
def update_student(student_id, name, email, phone, course, city):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE students
            SET name = ?,
                email = ?,
                phone = ?,
                course = ?,
                city = ?
            WHERE id = ?
        """, (name, email, phone, course, city, student_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("\nStudent updated successfully!")
        else:
            print("\nStudent ID not found!")

    except sqlite3.IntegrityError:
        print("\nError: Email already exists!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()




# DELETE: Remove a student using student ID
def delete_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM students
            WHERE id = ?
        """, (student_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print("\nStudent deleted successfully!")
        else:
            print("\nStudent ID not found!")

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()




# SEARCH: Find students by name
def search_student(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT * FROM students
            WHERE name LIKE ?
        """, ('%' + keyword + '%',))

        students = cursor.fetchall()

        if not students:
            print("\nNo matching student found!")
            return

        print("\nSearch Results:")

        for student in students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Email: {student['email']} | "
                f"Course: {student['course']} | "
                f"City: {student['city']}"
            )

    except sqlite3.Error as e:
        print("Database Error:", e)

    finally:
        conn.close()

