number = int(input("Введіть порядковий номер шуканого члена арифметичної прогресії: "))

first = 5
diff = 3

for i in range(1, number):
    first = first + diff
    
print (first)    
