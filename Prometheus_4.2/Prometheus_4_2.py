prise = 6500
euro_exchange_rate = float(input("Введіть курс євро до гривні: "))
summa = int(input("Введіть суму: "))
print((summa/euro_exchange_rate)//prise)
#print((int(input("Введіть суму: ")) / float(input("Введіть курс євро до гривні: "))) // prise)