days = int(input("Веедіть кількість днів: "))

hour = days * 24
minn = hour * 60
sec = minn * 60

print('{2:<10} {1:<10} {0:<10}'.format(sec, minn, days))
