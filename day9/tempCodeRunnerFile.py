import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "students.db"

connection = sqlite3.connect(DB_PATH)

print("Using database:", DB_PATH)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")


def add_student(name, age, department):
    cursor.execute("""
    INSERT INTO STUDENTS (name, age, department)
    VALUES (?,?,?)
    """, (name, age, department))

    connection.commit()
    print(f"{name} {age} {department} added to the database!")


def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

def search_student(student_id):
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id)
    )

    student = cursor.fetchone()

    if student:
        print(f"Student with ID {student_id} found!")
        print(student)
    else:
        print(f"No student found with ID {student_id}")
        
        
def update_student(student_id, department):
    cursor.execute(
        "UPDATE students SET department = ? WHERE id = ?",
        (department, student_id)
    )

    if cursor.rowcount > 0:
        connection.commit()
        print(f"Student {student_id} updated to {department}")
    else:
        print(f"No student found with ID {student_id}")
        
        

def delete_student(student_id):
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    
    if cursor.rowcount > 0:
        connection.commit()
        print(f"student with id {student_id} is deleted from database !")
    else:
        print(f"No student found with id {student_id}")
        
        
# to = input("Enter student id to delete :")
# delete_student(to)
    
# update_student(2,"Computer Science")
    

def show_menu():
    print("operations :")
    print("1.add_students")
    print("2.display_students")
    print("3.delete_students")
    print("4.update_student")
    
    
    


def perform_operation():
    choice = input("Enter your operation :")
    if choice == "1":
        name = input("Enter student name :")
        age = int(input("Enter student age :"))
        department = input("Enter student  deapartment name :")
        add_student(name, age, department)
    elif choice == "2":
        display_students()
    elif choice == "3":
        student_id = int(input("Enter student id to delete :"))
        delete_student(student_id)
    elif choice == "4":
        student_id = int(input("Enter student id to update :"))
        department = input("Enter new department name :")
        update_student(student_id, department)
    else:
        print("Enter valid operation ")
    
# name= input("Enter student name :")
# age= int(input("Enter student age :"))
# department= input("Enter student  deapartment name :")
# add_student(name,age,department)
# display_students()
# # search_student(4)
def ask_continue():
    choice = input("Do you want to continue? (y/n): ").strip().lower()
    return choice == "y"


def student_database():
    while True:
        show_menu()
        perform_operation()
        if not ask_continue():
            break

student_database()
connection.close()


# print("Students table created successfully")
