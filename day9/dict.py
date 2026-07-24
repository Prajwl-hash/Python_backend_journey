import json

students = [
    {
        "id": 1,
        "name": "Prajwal",
        "age": 22
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 21
    },
    {
        "id": 3,
        "name": "Kiran",
        "age": 20
    }
]

json_data = json.dumps(students)

print(json_data)