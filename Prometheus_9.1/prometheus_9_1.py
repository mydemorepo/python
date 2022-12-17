windows_count = int(input("Введіть кількість вікон "))
flors_count = int(input("Введіть кількість поверхів "))


class Building:
    pass


Building.windows_count = windows_count
Building.flors_count = flors_count

print('Загальна кількість вікон {0}'.format(Building.windows_count *
                                            Building.flors_count))
