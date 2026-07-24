class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department




name =input("Enter student name :")
age =int(input("Enter student age :"))
department =input("Enter student department name :")
student1 = Student(name,age,department)

student_data = [
    {
        "name": student1.name,
        "age": student1.age,
        "department": student1.department
    }
]

print(student_data)