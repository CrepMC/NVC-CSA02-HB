class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.__mileage = mileage
    def show_info(self):
        print(f"This car is {self.color}. It gone {self.__mileage} km.")
    def get_mileage(self):
        return self.__mileage

green_car = Car('Green', 20)
red_car = Car('Red', 30)


green_car.__mileage = 25
print(green_car.get_mileage())

# ... print thông tin ...