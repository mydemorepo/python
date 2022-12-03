# Adam Vasyliuta
# 03.12.2022

number = int(input("Введіть число: "))

print(f'{number//1000 } + \
{(number//100)%10} + \
{(number//10)%10} + \
{number%10} = \
{number//1000 + (number//100)%10 + (number//10)%10 + number%10}')
