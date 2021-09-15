#   Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

print("Script to calculate the area and perimeter of a rectangle")
leng = float(input("Length: "))
width = float(input("Width: "))

area = leng * width
perimeter = 2*(leng+width)

print(f"The Area is {area} and the perimeter is {perimeter} ")