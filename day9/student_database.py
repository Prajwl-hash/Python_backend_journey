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
    
    
    
name= input("Enter student name :")
age= int(input("Enter student age :"))
department= input("Enter student  deapartment name :")
add_student(name,age,department)
display_students()
# search_student(4)


connection.close()


# print("Students table created successfully")
