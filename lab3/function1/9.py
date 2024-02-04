def calculate_sphere_volume(radius):
    pi = 3.14159
    volume = (4/3) * pi * (radius ** 3)
    return volume

radius = 5
volume = calculate_sphere_volume(radius)
print(f"The volume of a sphere with radius {radius} is {volume}.")