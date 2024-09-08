class Car:
    def __init__(self, model, color, manufacturer):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer

    def describe_car(self):
        return f"My dream car is a {self.color} {self.manufacturer} {self.model}."


dream_car = Car("Model S", "Red", "Tesla")

dream_car.describe_car()
print(dream_car.describe_car())
