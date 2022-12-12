test_str = "2 -1 9 6"
summa = 0

test_list = test_str.split(' ')
for i in test_list:
    summa += float(i)

print(summa)
