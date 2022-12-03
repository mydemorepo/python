distance = float(input("Веедіть відстань: "))

inches = distance * 39.37
feet = distance * 3.28
miles = distance * 0.000621371
yards = distance * 1.0936

print('{0:.2f} {1:.2f} {3:.2f} {2:.2f}'.format(inches, feet, miles, yards))
