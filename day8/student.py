students = ["Prajwal", "Rahul", "Ankit", "Kiran"]


# Functions
def remove(to_delete):
    if to_delete in students:
        students.remove(to_delete)
        print(f"{to_delete} removed from the list")

    else:
        print("Enter valid student name")


def search_student(to_search):
    if to_search in students:
        print(f" {to_search} Found in the list")
    else:
        print("Student not found")


def add_student(name):
    students.append(name)
    print(f"{name} added to the list ")


def display_students():
    print (students)


# list operation select

def show_menu():
    print("operations :")
    print("1.add student")
    print("2.remove student")
    print("3.search student")
    print("4.display student")
    print("5.Exit")


# perform operation
def perform_operation():
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the name of the student to add: ")
        add_student(name)

    elif choice == "2":
        to_delete = input("Enter student name to delete: ")
        remove(to_delete)

    elif choice == "3":
        to_search = input("Student to search: ")
        search_student(to_search)

    elif choice == "4":
        display_students()
    
    elif choice == "5":
        return True


# controller function
def student():
    while True:
        show_menu()
        if perform_operation():
            break


student()
          
        
        

     
        



