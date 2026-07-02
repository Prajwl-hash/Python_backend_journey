# simple interest 
# formula {SI= P * R * T } /100

Principal_amount = float(input("Enter your principle amount:"))
Interest_rate  = float(input("Enter your Interest rate:"))
Time__period = float(input("Enter time period of the loan:"))

Interest =( Principal_amount * Interest_rate * Time__period )/100
print("=========================================")
print("Simple interest calculator")
print("=========================================")
print(f"Principal Amount :{Principal_amount}")
print(f"Interest Rate    :{Interest}")
print(f"Time Period      :{Time__period}")
print(f"\nhere is your simple interest you have to pay :₹{Interest:.2f}rupees")
print("=========================================")

