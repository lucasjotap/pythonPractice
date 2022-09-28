class Car():
    """Car model"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) +' '+ self.make +' '+ self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
            
    def updt_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the chenge if it attempts to roll the odometer back.
        """
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles        
 
# Creating child class.
class ElectricCar(Car):
    """Aspects of an electric vehicle"""
    def __init__(self, make, model, year):
        """
        Initialiaze attributes of the parent class.
        Then initialize attibutes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -hWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.describe_battery())
print(my_tesla.get_name())

