side1, side2, side3 = map(int, input("Enter the 3 sides of a triangle in order: ").split())
if side1 == side2 == side3:
    print("It's an Equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("It's an Isosceles triangle.")
else:
    print("It's a Scalene triangle.")
