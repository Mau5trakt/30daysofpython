#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)

print("Script to calculate the perimeter of a triangle")
side_a = float(input("side a: "))
side_b = float(input("side b: "))
side_c = float(input("side c: "))

perimeter = side_a + side_b + side_c

print(f"The perimeter of the triangle is {perimeter}")