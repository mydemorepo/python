number = int(input("Введіть число: "))
mydict = {}

for i in range(0, number + 1):
    mydict[i] = i ** 2

print(mydict)
