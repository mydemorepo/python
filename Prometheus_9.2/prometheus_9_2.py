car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")


class Cars:
    list_of_cars = list()


Cars.list_of_cars.append(car_1)
Cars.list_of_cars.append(car_2)
Cars.list_of_cars.append(car_3)

print('Список авто: {0}'.format(" та ".join(Cars.list_of_cars)))
