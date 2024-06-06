class User:
    def __init__(self,first_name,last_name,is_online,points,login_attempts):
        self.first = first_name
        self.last = last_name
        self.status = is_online
        self.no_of_points = points
        self.login = login_attempts
    
    def describe_user(self):
        print(f"The User is Known as {self.first} better known as {self.last} who currently is {self.status} and has accumulated a total of {self.no_of_points} dabbloons\n")
    
    def greet_user(self):
        print(f"Hello and Welcome Back {self.first} {self.last}\nGlad to have you back!\n")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    def increment_login_attempts(self):
        self.login += 1
        print(f"The amount after incrementing is {self.login}\n")
    def reset_login_attempts(self):
        self.login = 0
        print(f"The amount of login attempts has been reset current counter = {self.login}")
user1 = User("Raven","kapur","online",480,12)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()
user2 = User("David","Sisodia","offline",800,34)
user2.describe_user()
user2.greet_user()
user3 = User("Mary","Bloom","online",6000,333)
user3.describe_user()
user3.greet_user()

# Inheritance
# class Admin(User):
#     def __init__(self,first_name,last_name,is_online,points,login_attempts):
#         super().__init__(first_name,last_name,is_online,points,login_attempts= 0)
#         print(f"Name:{first_name} {last_name},Current Status:{is_online},Points:{points}")
#         self.privileges =["Can ADD post","Can BAN user","Can DELETE posts","Can DELETE replies"]
#     def show_privileges(self):
#         print(self.privileges)

# isAdmin = Admin("Adam","Fring","Online",500,1)
# isAdmin.show_privileges()

class Admin(User):
    def __init__(self,first_name,last_name,is_online,points,login_attempts):
        super().__init__(first_name,last_name,is_online,points,login_attempts= 0)
        print(f"Name:{first_name} {last_name},Current Status:{is_online},Points:{points}")
        self.pv = privileges()

class privileges:
    def __init__(self):
        self.pvs = ["Can BAN user","Can DELETE posts","Can DELETE replies","Can ADD posts"]
    def show_privileges(self):
        print(self.pvs)

isAdmin = Admin("Adam","Fring","Online",500,1)
isAdmin.pv.show_privileges()