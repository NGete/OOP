# Base class
class Entity:
    def move(self):
        pass  # Placeholder method to be overridden in subclasses

# Animal subclasses
class Dog(Entity):
    def move(self):
        return "Running 🐕"

class Bird(Entity):
    def move(self):
        return "Flying 🦅"

# Vehicle subclasses
class Car(Entity):
    def move(self):
        return "Driving 🚗"

class Plane(Entity):
    def move(self):
        return "Flying ✈️"

# Using polymorphism
entities = [Dog(), Bird(), Car(), Plane()]

for entity in entities:
    print(f"{entity.__class__.__name__}: {entity.move()}")