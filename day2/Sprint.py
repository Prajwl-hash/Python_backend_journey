# Login system v2

admin_password = "hello"
teacher_password = "hi"
student_password = "whatsup"

# only allow - student - teacher - admin

role = input("enter your role :").lower().strip()
# password = input("enter your password:")

if role == "admin":
    password = input("Enter your password: ")
    if password == admin_password:
        print("login successful!Welcome,admin!")
    else:
        print("invalid credentials,enter correct password.")


elif role == "teacher":
    password = input("Enter your password: ")
    if password == teacher_password:
     print("login successful!Welcome, teacher!")
    else:
        print("invalid credentials,enter correct password.")


elif role == "student":
    password = input("Enter your password: ")
    if password == student_password:
        print("login successful!Welcome, student!")
    else:
        print("invalid credentials,enter correct password.")

else:
    print("Invalid role")