import math


v0 = 5 
alpha_deg = 40  
g = 9.80665  

alpha_rad = math.radians(alpha_deg)

x_max = v0 * math.cos(alpha_rad)
y_max = v0 * math.sin(alpha_rad) - 0.5 * g * x_max**2

print(f"Дальность прыжка: {x_max:.2f} м")
print(f"Высота прыжка: {y_max:.2f} м")
