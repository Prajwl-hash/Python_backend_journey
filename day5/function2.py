def square(number):
    return number ** 2

def cube(number):
    return number ** 3
def area_of_square(side):
    return square(side)
area = area_of_square(6)
print(f"Cube of the number: {cube(3)}")
print(f"Square of the number: {square(5)}")
print(f"Area of the square: {area_of_square(6)}")