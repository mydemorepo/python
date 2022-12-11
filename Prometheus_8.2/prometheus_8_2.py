number = int(input("Введіть число "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
flag = False
for i in range(0, 11):
    if (a[i] == number):
        flag = True
if (flag):
    print("Введене число - існує")
else:
    print("Введене число - не існує")
