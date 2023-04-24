# if you don't want to give anything under the function you can give pass
# PascalCase- first letter capital
# camelCase- first letter small
# snake_case- all small but separated by "_"


class UserTest:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age


new_user = UserTest("Tamil", 26)


