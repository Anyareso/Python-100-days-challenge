# Creating classes/declaring
class User:
    # Initialize attributes
    # self is the actual attribute being created
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)

# # Initializing an object from a class
# user_1 = User("001", "angela")
# # Creating an attribute for a class
# print(user_1.user_name)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "doe"
