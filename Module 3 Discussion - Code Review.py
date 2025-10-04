class user:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"Name = {self.first_name} {self.last_name}")
        print(f"Age = {self.age}")
        print(f"Email = {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, hope you are having a wonderful day.\n")

user1 = user("Henry", "Cavhill", "50", "C.henry@gmail.com")
user2 = user("Tom", "Holland", "26", "spideyboi@gmail.com")
user3 = user("Scarlett", "Johension", "32", "S.jojo@gmail.com")
user4 = user("Bat", "Man", "40", "vengenceseeker123@gmail.com")
user5 = user("Chrish", "Evans", "80", "peggylover@gmail.com")
       
users = [user1, user2, user3, user4, user5]

for user in users:
    user.describe_user()
    user.greet_user()