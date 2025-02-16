class Car:
    def __init__(self, color, mileage):
      self.color = color
      self.mileage = mileage
    def show_info(self):
        print(f"The car is {self.color}, it have gone for {self.mileage} km")
        
green_car = Car('Green', 20)
red_car = Car('red', 30)

green_car.show_info()