# calculator.py

def add(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b


def show_menu():
    print("operations :")
    print("1.add")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    
def ask_continue(a,b):
    print("do you want to do another operation? Y/N")
    response =input("__").upper()
        
    if response == "Y":
        return True
    else:
        return False
        
        
    
    


def perform_operation(a, b):
    
        choice = input("Enter your operation :")
        if choice == "1":
            print(add(a, b))
        elif choice == "2":
            print(subtraction(a, b))
        elif choice == "3":
            print(multiplication(a, b))
        elif choice == "4":
            print(division(a, b))
        else:
            print("Enter valid operation ")
            
       
            
        


def calculate():
    while True:
         a = int(input("enter the first number :"))
         b = int(input("enter the second number number :"))

         show_menu()
         perform_operation(a, b)
         if not ask_continue():
          break
        


calculate()
