
# Import database and student functions
from database import create_table
from student import (
    add_student,
    display_students,
    update_student,
    delete_student,
    search_student
)


# Function to accept student information
def get_student_details():

    print("\nEnter Student Information")

    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()
    course = input("Enter Course: ").strip()
    city = input("Enter City: ").strip()

    # Basic input validation
    if not all([name, email, phone, course, city]):
        print("\nAll fields are required!")
        return None

    if "@" not in email or "." not in email:
        print("\nPlease enter a valid email address!")
        return None

    if not phone.isdigit():
        print("\nPhone number must contain digits only!")
        return None

    return name, email, phone, course, city


# Main menu function
def main():

    # Create database and table
    create_table()

    while True:

        print("\n")
        print("=" * 45)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        print("=" * 45)

        choice = input("Enter Your Choice (1-6): ").strip()

        # CREATE
        if choice == "1":

            details = get_student_details()

            if details:
                add_student(*details)

        # READ
        elif choice == "2":

            display_students()

        # UPDATE
        elif choice == "3":

            try:
                student_id = int(input("Enter Student ID: "))

                details = get_student_details()

                if details:
                    update_student(student_id, *details)

            except ValueError:
                print("\nPlease enter a valid numeric ID!")

        # DELETE
        elif choice == "4":

            try:
                student_id = int(input("Enter Student ID: "))

                confirm = input(
                    "Are you sure you want to delete? (y/n): "
                ).lower()

                if confirm == "y":
                    delete_student(student_id)
                else:
                    print("\nDelete operation cancelled!")

            except ValueError:
                print("\nPlease enter a valid numeric ID!")

        # SEARCH
        elif choice == "5":

            keyword = input("Enter Student Name: ").strip()

            if keyword:
                search_student(keyword)
            else:
                print("\nPlease enter a search keyword!")

        # EXIT
        elif choice == "6":

            print("\nThank you for using Student Management System!")
            break

        else:

            print("\nInvalid choice! Please select 1 to 6.")


# Application entry point
if __name__ == "__main__":
    main()
