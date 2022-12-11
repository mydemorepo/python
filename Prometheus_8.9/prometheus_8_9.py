user = {
       'name': 'sergii',
       'age': 100500,
       'country': 'Ukraine'
}

key = input("Введіть ім'я ключа ")
new_key = input("Введіть нове ім'я ключа ")

if (key not in user):
    print("Шуканого ключа немає")
else:
    user[new_key] = user[key]
    user['country'] = 'Ukraine'
    del user[key]
    del user['country']
    user['country'] = 'Ukraine'
    print(user)
