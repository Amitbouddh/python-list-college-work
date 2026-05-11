class Car:

    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def details(self):
        return f"I have a car of {self.brand}, color of {self.color} and mileage is {self.mileage} km/l"


# Creating objects
c1 = Car("BMW", "Black", 34)
c2 = Car("Tesla", "White", 32)

print(c1.details())
print(c2.details())