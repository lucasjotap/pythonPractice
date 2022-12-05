class Dog():

    def __init__(self, name, age) -> None:
        """Creating a dog class"""
        self.name = name
        self.age = age

    def say_hi(self):
        """Print hello"""
        print(f"{self.name.title()} says hi!")

    def sit_down(self):
        """Simulating a dog sitting down"""
        print(f"{self.name.title()} sat down.")

    def roll_over(self):
        """Simulating a dog rolling over."""
        print(f"{self.name.title()} rolled over.")

new_dog = Dog('Milo', 5)

new_dog.say_hi()
new_dog.sit_down()
new_dog.roll_over()
