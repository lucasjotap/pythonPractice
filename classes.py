class Restaurant():
    """Model of a restaurant"""
    def __init__(self, name, cuisine):
        """Initialize restaurant"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        """Describes restaurant's name and cuisine"""
        vowels = "aeiou"
        if self.cuisine[0] in vowels:
            print(self.name.title() + " is an " + self.cuisine.title() + ' restaurant.')
        else:
            print(self.name.title() + " is a " + self.cuisine.title() + ' restaurant.')

    def open_restaurant(self):
        """Display open sign."""
        print(self.name.title() + " is now open")

    def set_number_served(self, new_served):
        """Set the number of customers that have been served."""
        self.number_served += new_served
        i = "Number of served customers: " + str(self.number_served)
        return i

    def increment_number_served(self, increment):
        """Increments served numbers of customers"""
        self.number_served += increment      
