wheels_count = int(input("Введіть кількість коліс "))
sits = int(input("Введіть кількість місць "))
guns_count = int(input("Введіть кількість зброї "))


class Banderomobil:
    cars_count = 0

    def __init__(self, wheels_count, sits, guns_count):
        self.wheels_count = wheels_count
        self.sits = sits
        self.guns_count = guns_count
        Banderomobil.cars_count += 1

    def print_info(self):
        print(("Бандеромобіль на {0} колесах, " +
               "призначений для {1} людей і {2}" +
               " стволів").format(self.wheels_count,
                                  self.sits,
                                  self.guns_count))


car1 = Banderomobil(wheels_count, sits, guns_count)
car1.print_info()
print(car1.cars_count)

car2 = Banderomobil(wheels_count + 1, sits + 1, guns_count + 1)
car2.print_info()
print(car2.cars_count)
