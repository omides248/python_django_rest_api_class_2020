class User:
    count_users = 0

    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        # self.add_count()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_customer(self):
        return True if self.role == "customer" else False

    @classmethod
    def add_count(cls):
        cls.count_users += 1


user_1_obj = User("omid", "esmaeili", "customer")
user_2_obj = User("hasan", "hasssss", "manager")

print(user_1_obj.full_name)

# print(user_1_obj.first_name)
# print(user_1_obj.last_name)
# print(user_1_obj.role)
# print(user_1_obj.count_users)
# print(user_2_obj.count_users)
# print(user_1_obj.is_customer())
# print(user_2_obj.is_customer())
# User.add_count()
# User.add_count()
# User.add_count()
# User.add_count()
# print(User.count_users)
print(user_2_obj.count_users)
print(user_1_obj.count_users)
