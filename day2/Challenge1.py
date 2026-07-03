# take two numbers from user and print arithematic op

first_number = float(input("Enter your first number :"))
second_number = float(input("Enter your second number :"))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
modulus = first_number % second_number
power = first_number ** second_number


print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")
print(f"floor Division : {floor_division}")
print(f"Modulus        : {modulus}")
print(f"Power          : {power}")
