class Users():
    """Model of an app user"""
    def __init__(self, name, l_name, phone, age):
        """Describe an user"""
        self.name = name
        self.l_name = l_name
        
        self.age = age

    def describe_user(self):
        """Describe an app user"""
        user = self.name.title() +' '+ self.l_name.title() + " is " + str(self.age) + " years-old"
        print(user)
    
    def greet_user(self):
        """Greet the user"""
        print("Hello " + self.name.title() + "\n")

x = Users('mark','berry', 'iphone 8', 45)
x.describe_user()
x.greet_user()

y = Users('samantha','christie', 'iphone 10', 22)
y.describe_user()
y.greet_user()

a = Users('ava','lovelace', 'iphone 13', 30)
a.describe_user()
a.greet_user()

b = Users('sean','carrol', 'iphone 8', 50)
b.describe_user()
b.greet_user()
