

def circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

def square(a):
    area = a * a
    perimeter = 4 * a
    return area, perimeter

# radius = 5
# circle_area, circle_circumference = circle(radius)

# length = 5
# square_area, square_perimeter = square(length)

# print(f"The area of the circle with radius {radius} is {circle_area}")
# print(f"The circumference of the circle with radius {radius} is {circle_circumference}")
# print(f"The area of the square with length {length} is {square_area}")
# print(f"The perimeter of the square with length {length} is {square_perimeter}")
