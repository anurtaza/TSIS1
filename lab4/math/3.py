import math

num_of_sides = int(input())
length = int(input())

area = (num_of_sides * length**2) / (4 * math.tan(math.pi / num_of_sides))

print(area)