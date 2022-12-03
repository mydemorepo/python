number = int(input("Введіть число"))


def is_even_or_odd(number):
    if (number % 2 == 0):
        return "число " + str(number) + " парне"
    else:
        return "число " + str(number) + " непарне"


print(is_even_or_odd(number))
