class User:
    #crete a constructor that will creates starting variables for our objects
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


#creating an object from the class user
# user_1 = User()
#
# #creating attributes for the object (things an object will have)
# user_1.name = "Dicky"
# user_1.id = "A01"

user_1 = User(1, "loki")
user_3 = User(12, "dom")

user_1.follow(user_3)

print(user_1.following)



