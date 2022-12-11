last_name = input("Введіть прізвище: ")
name = input("Введіть ім'я: ")
second_name = input("Введіть по батькові: ")

if (len(last_name) < 1 or len(name) < 1 or len(second_name) < 1):
    print("Не введений ключовий параметр")
else:
    print('{0} {1}{2}'.format(last_name, name.replace(name[1:], '.'),
                              second_name.replace(second_name[1:], '.',)))
