# Secret Number Guessing Game.

secret_number = 7
while True:
    guess = int(input("Guess the number :"))
    difference = secret_number - guess
    if secret_number == guess:
        print("Congratulations!")
        break
    elif difference >= 4:
        print("Too low!")
    elif 2 >= difference <= 3:
        print("low")
    elif difference == 1:
        print(" very close")
    elif difference == -1:
        print(" very close")
    elif -3 >= difference <= -2:
        print("High")
    elif difference <= -4:
        print("Too high")
