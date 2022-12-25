name = input("Введіть ім'я користувача  ")
new_name = input("Введіть нове ім'я користувача ")
new_last_name = input("Введіть нове прізвище користувача ")
new_second_name = input("Введіть нове по батькові користувача ")


class User:
    count_users = 0

    def __init__(self, name):
        self.name = name
        User.count_users += 1

    def change_username(self, username):
        self.name = username

    @classmethod
    def get_count(cls):
        return cls.count_users

    @staticmethod
    def prepare_name(name, last_name, second_name):
        return '{1} {0}{2}'.format(name.replace(name[1:], '.'),
                                   last_name,
                                   second_name.replace(second_name[1:], '.'))


new_username = User.prepare_name(new_name, new_last_name, new_second_name)

user1 = User(name)
print(user1.name)
print(User.count_users)
print(user1.count_users)
user1.change_username(new_username)
print(user1.name)


user2 = User(name)
print(User.count_users)
print(user2.count_users)
