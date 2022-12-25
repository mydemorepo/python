input_qa_name = input("Введіть ім'я тестувальника: ")
input_pm_name = input("Введіть нове ім'я менеджера: ")
input_qa_expected_action = input("Введіть очікувану дію для тестувальника: ")
input_pm_expected_action = input("Введіть очікувану дію для менеджера: ")
input_qa_task = input("Введіть поставлену задачу тестувальнику: ")


class User:

    def __init__(self, username, expected_action):
        self._username = username
        self._expected_action = expected_action

    def perform_action(self):
        print("{0} виконує дію: \'{1}\'".format(self._username,
                                                self._expected_action))

    def get_username(self):
        return self._username

    def set_username(self, value):
        self._username = value
        self._username = self._username.title()


class QA(User):

    def __init__(self, username, expected_action, tasks=list()):
        super().__init__(username, expected_action)
        self.tasks = tasks

    def set_task(self, task):
        self.tasks.append(task)


class Manager(User):

    def __init__(self, username, expected_action):
        super().__init__(username, expected_action)

    def perform_action(self):
        print("Зайнятий. Напишіть мені листа з Вашим питанням")


qa = QA(input_qa_name, input_qa_expected_action)
print(qa.get_username())
qa.set_username(input_qa_name)
print(qa.get_username())
qa.perform_action()
print(qa.tasks)
qa.set_task(input_qa_task)
print(qa.tasks)

pm = Manager(input_pm_name, input_pm_expected_action)
print(pm.get_username())
pm.set_username(input_pm_name)
print(pm.get_username())
pm.perform_action()
