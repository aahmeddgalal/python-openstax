import math

b = float(input("b: "))
a = float(input("a: "))
c = float(input("c: "))

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a) 

print("x1: ", x1)
print("x2: ", x2)