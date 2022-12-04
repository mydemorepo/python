import math

x1 = math.radians(float(input("Введіть широту першої точки: ")))
y1 = math.radians(float(input("Введіть довготу першої точки: ")))
x2 = math.radians(float(input("Введіть широту другої точки: ")))
y2 = math.radians(float(input("Введіть довготу другої точки: ")))

print('{0:>10.3f}'.format(6371.032 * math.acos(math.sin(x1) *
                          math.sin(x2) +
                          math.cos(x1) *
                          math.cos(x2) *
                          math.cos(y1 - y2))))
