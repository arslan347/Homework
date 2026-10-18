import math

def calculate_rectangle_area(width, height):
    return width * height
  
def calculate_circle_area(radius):
    return math.pi * radius * radius
  
print("прямоугольник:")
w = float(input("ширина: "))
h = float(input("высота: "))

print(f"площадь: {calculate_rectangle_area(w, h):.2f}")

print("круг:")
r = float(input("радиус: "))

print(f"площадь: {calculate_circle_area(r):.2f}")
