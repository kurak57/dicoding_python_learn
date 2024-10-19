class Car:
    def __init__(self, brand, type, color, year):
        self.brand = brand
        self.type = type
        self.color = color
        self.year = year

    def drive(self):
        print("car is driving")

    def stop(self):
        print("car was stopped")