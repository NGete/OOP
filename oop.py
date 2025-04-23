# Base class (Superhero)
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name  # Public attribute
        self._power = power  # Protected attribute
        self.__strength_level = strength_level  # Private attribute

    def use_power(self):
        return f"{self.name} uses {self._power}!"

    def get_strength(self):  # Encapsulation (Getter)
        return self.__strength_level

    def set_strength(self, new_level):  # Encapsulation (Setter with validation)
        if new_level > 0:
            self.__strength_level = new_level
        else:
            print("Strength level must be positive!")

# Subclass (Different Type of Hero with Polymorphism)
class Speedster(Superhero):
    def __init__(self, name, strength_level, speed):
        super().__init__(name, "Super Speed", strength_level)
        self.speed = speed  # New attribute specific to Speedster

    def use_power(self):  # Method Overriding (Polymorphism)
        return f"{self.name} runs at {self.speed} km/h!"

# Creating objects
hero1 = Superhero("Titan", "Flight", 90)
speedster1 = Speedster("Blaze", 75, 500)

# Accessing methods
print(hero1.use_power())  # Titan uses Flight!
print(speedster1.use_power())  # Blaze runs at 500 km/h!

# Encapsulation example
print(hero1.get_strength())  # Accessing private attribute safely
hero1.set_strength(95)  # Updating strength level
print(hero1.get_strength())  # Updated strength level