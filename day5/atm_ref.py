def get_pin():
    pin = input("Enter your pin: ")
    return pin


def is_pin_correct(pin, correct_pin):
    return correct_pin == pin


def pin_response(pin_match):
    if pin_match == True:
        print("Welcome to the atm!")
    else:
        print("Maximun attempts reached. Please try again later.")


def atm():
    failed_attempts = 0
    correct_pin = "1234"
    
    while failed_attempts < 3:
        atm_pin = get_pin()
        if is_pin_correct(atm_pin, correct_pin):
            pin_response(True)
            return
        failed_attempts += 1

    pin_response(False)


atm()
