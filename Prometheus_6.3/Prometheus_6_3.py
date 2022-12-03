number = int(input("Введіть число"))

i = 0
while(i <= number):
    if (i % 2 == 0):
        print(i ** 2)
    else:
        print(i)
    i += 1
