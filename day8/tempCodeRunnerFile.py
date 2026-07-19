students = ["Prajwal","Rahul","Ankit","Kiran"]

def remove(name):
    if name in students:
        students.remove(name)
        print(f"{name} removed from the list")
        
    else:
        print("Enter valid student name")
        
        
def search_student(to_search):
    if to_search in students:
        print(f" {to_search} Found in the list")
    else:
        print("Student not found")
        
        
    



def student():

     name =input("Enter the name of the student to remove:")
     
     remove(name)
     to_search = input("Student to seacrh :")
     search_student(to_search)
     
     
     
     

student()
print(students)
    

