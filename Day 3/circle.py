#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("Circle Radius")
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * (radius**2)
circumference = 2 * pi * radius
print(f"The area of the circle is: {area} and the circumference is {circumference}")