correct_pin = "1234"
pin = input("Enter the atm pin:")
failed_attempts = 0

while pin != correct_pin and failed_attempts < 3:
    print("Wrong pin .")
    failed_attempts += 1
    pin = input("Enter the ATM PIN:")


if pin == correct_pin:
    print("Welcome to the atm!")

else:
    print("Maximun attempts reached. Please try again later.")
