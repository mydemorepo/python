miles = float(input("Введіть кількість миль"))


def convert_miles_to_km(miles):
    km = miles * 1.6
    return round(km, 2)


print(convert_miles_to_km(miles))
