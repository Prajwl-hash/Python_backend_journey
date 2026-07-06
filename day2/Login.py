role = input("Enter role: ").lower().strip()
password = input("Enter your password :")

if role == "admin" and password == "ad-pass":
    print("Welcome admin")

elif role == "teacher" and password == "te-pass":
    print("Welcome teacher")

elif role == "student" and password == "stu-pass":
    print("Welcome student")

else:
    print("Invalid credentials")
