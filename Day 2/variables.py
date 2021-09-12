#Day 2 of 30 days of python programming
import math
first_name = "Enrique"
last_name = "Alemany"

full_name = first_name +" "+ last_name

country = "Nicaragua"

City = "Managua"

age = 20

year = 2021

is_maried = False

is_true = True

is_light_on = True

exam1 = "Estadística"; exam2 = "Química Analitica & Estadística"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(City))
print(type(age))
print(type(year))
print(type(is_maried))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

num_one = 3
num_two = 4
print(f"The first number is: {num_one} and the second one is {num_two}")
total = num_one + num_two
print("The total is {}".format(total))
diff = num_two - num_one
print(diff)
product = num_one * num_two
print(product)
division = num_two / num_one
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor = num_two // num_one
print(floor)

radius = 30

area = math.pi * (radius**2)

print(f"The Area of the circle with radius {radius} m. is: {area} sqr meters" )

circunference = 2 * math.pi * radius

print(f"The length of the circunference is: {circunference}")

inradio = int(input("Enter the Radius of the circle in meters: "))
inarea = math.pi * (inradio**2)
print(f"The radio is {inarea}")


