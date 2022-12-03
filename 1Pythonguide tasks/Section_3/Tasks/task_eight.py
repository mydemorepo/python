# Temperature calculator

t = float(input("Введіть значення температури: "))

f = 32 + (9 / 5) * t
k = t + 273.15

print('{1:^15.2f} {0:^15.2f}'.format(k, f))
