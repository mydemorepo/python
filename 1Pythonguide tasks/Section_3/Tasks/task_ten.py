import math

x1 = float(input("Введіть широту першої точки: "))
y1 = float(input("Введіть довготу першої точки: "))
x2 = float(input("Введіть широту другої точки: "))
y2 = float(input("Введіть довготу другої точки: "))

print('{0:>10.3f}'.format(6371.032 *
                  math.acos(math.sin(math.radians(x1)) *
                            math.sin(math.radians(x2)) *
                            math.cos(math.radians(x1)) *
                            math.cos(math.radians(x2)) *
                            math.cos(math.radians(y1) - math.radians(y2)))))
